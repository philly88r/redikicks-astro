#!/usr/bin/env python3
"""
Generate images for Redikicks articles using fal.ai
"""

import requests
import os
import time

FAL_KEY = os.environ.get('FAL_KEY')
if not FAL_KEY:
    print("Error: FAL_KEY not found")
    exit(1)

# Image generation configurations for each article
articles = [
    {
        "slug": "best-affordable-mens-watches-under-100",
        "prompts": [
            "Professional product photography, luxury men's wristwatch on wooden surface, natural lighting, masculine aesthetic, high quality magazine style, dark background with accent lighting, detailed dial visible",
            "Collection of affordable men's watches arranged artistically, various styles including dress and casual watches, black background, professional product photography, high-end catalog style",
            "Man's wrist wearing elegant timepiece, close-up shot, business casual attire, natural window lighting, shallow depth of field, lifestyle photography"
        ]
    },
    {
        "slug": "first-date-tips-for-men",
        "prompts": [
            "Candid lifestyle photography, confident man on date at restaurant, natural warm lighting, stylish casual outfit, genuine smile, professional editorial style, romantic atmosphere",
            "Well-dressed man opening door for date, chivalrous gesture, evening setting, street lights bokeh background, fashion photography style",
            "Couple having engaging conversation at cozy cafe, man looking confident and attentive, warm ambient lighting, lifestyle magazine photography"
        ]
    },
    {
        "slug": "how-to-negotiate-salary-raise",
        "prompts": [
            "Professional office setting, confident man in business meeting, firm handshake, modern corporate environment, natural lighting, executive boardroom",
            "Man presenting with confidence in meeting room, pointing at charts, professional attire, bright modern office, corporate photography style",
            "Professional man reviewing documents at desk, focused expression, success-oriented atmosphere, clean minimalist office, natural window light"
        ]
    },
    {
        "slug": "best-home-workout-equipment-for-men",
        "prompts": [
            "Modern home gym setup, adjustable dumbbells, kettlebells on rack, clean minimalist garage space, natural window lighting, fitness magazine photography",
            "Man doing push-ups at home gym, resistance bands visible, motivational atmosphere, bright lighting, athletic lifestyle photography",
            "Home workout space with pull-up bar, yoga mat, compact equipment organized, morning sunlight, inspiring fitness environment"
        ]
    },
    {
        "slug": "camping-essentials-for-beginners",
        "prompts": [
            "Outdoor adventure photography, camping gear laid out on grass, tent in background, golden hour lighting, wilderness mountain setting, high quality magazine style",
            "Campsite at dusk with warm lantern glow, tent pitched perfectly, camping chairs and equipment arranged, peaceful nature setting, adventure photography",
            "Person setting up camping equipment, hands arranging gear, forest background, morning light, outdoor lifestyle photography"
        ]
    }
]

headers = {
    "Authorization": f"Key {FAL_KEY}",
    "Content-Type": "application/json"
}

def generate_image(prompt, output_path):
    """Generate image using fal.ai"""
    url = "https://fal.run/fal-ai/flux/dev"
    
    payload = {
        "prompt": prompt,
        "image_size": "landscape_4_3",
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": True
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        if response.status_code == 200:
            data = response.json()
            if 'images' in data and len(data['images']) > 0:
                image_url = data['images'][0]['url']
                # Download the image
                img_response = requests.get(image_url, timeout=60)
                if img_response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"✅ Generated: {output_path}")
                    return True
        print(f"❌ Failed to generate: {output_path}")
        print(f"Response: {response.status_code} - {response.text[:200]}")
        return False
    except Exception as e:
        print(f"❌ Error generating {output_path}: {str(e)}")
        return False

# Generate all images
output_dir = "public/images"
os.makedirs(output_dir, exist_ok=True)

total_images = 0
successful = 0

for article in articles:
    print(f"\n📝 Processing: {article['slug']}")
    for i, prompt in enumerate(article['prompts'], 1):
        output_path = f"{output_dir}/{article['slug']}-{i}.jpg"
        total_images += 1
        
        if generate_image(prompt, output_path):
            successful += 1
        
        # Rate limiting
        time.sleep(2)

print(f"\n{'='*60}")
print(f"✅ COMPLETE: {successful}/{total_images} images generated")
print(f"{'='*60}")
