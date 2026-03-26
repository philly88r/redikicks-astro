#!/usr/bin/env python3
"""
Update articles with generated images and Amazon products
"""

import os
import re

# Amazon product data for each article
amazon_products = {
    "best-affordable-mens-watches-under-100": [
        {
            "name": "Casio MDV106-1A Duro Analog Watch",
            "price": "$69.95",
            "rating": "4.6",
            "url": "https://www.amazon.com/dp/B00JFI6F4E?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71W-M+GZXjL._AC_UY679_.jpg"
        },
        {
            "name": "Timex Weekender 40mm Watch",
            "price": "$39.99",
            "rating": "4.5",
            "url": "https://www.amazon.com/dp/B004VR9GCQ?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71kG+Zv+GvL._AC_UY679_.jpg"
        },
        {
            "name": "Seiko 5 Automatic SNK809",
            "price": "$95.00",
            "rating": "4.7",
            "url": "https://www.amazon.com/dp/B000LTAY2U?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71L8hlT1PXL._AC_UY679_.jpg"
        },
        {
            "name": "Citizen Eco-Drive BM8180-03E",
            "price": "$89.99",
            "rating": "4.6",
            "url": "https://www.amazon.com/dp/B000EQR6H0?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71j1qOXOYZL._AC_UY679_.jpg"
        },
        {
            "name": "Fossil Minimalist FS5304",
            "price": "$79.99",
            "rating": "4.5",
            "url": "https://www.amazon.com/dp/B01N0QKHXM?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71LgKw8QQPL._AC_UY679_.jpg"
        }
    ],
    "best-home-workout-equipment-for-men": [
        {
            "name": "Bowflex SelectTech 552 Adjustable Dumbbells",
            "price": "$429.00",
            "rating": "4.8",
            "url": "https://www.amazon.com/dp/B001ARYU58?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71+pOdQ1jhL._AC_SL1500_.jpg"
        },
        {
            "name": "Fit Simplify Resistance Loop Bands",
            "price": "$12.95",
            "rating": "4.5",
            "url": "https://www.amazon.com/dp/B01AVDVHTI?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71xU+N9KwJL._AC_SL1500_.jpg"
        },
        {
            "name": "Iron Gym Total Upper Body Workout Bar",
            "price": "$29.99",
            "rating": "4.4",
            "url": "https://www.amazon.com/dp/B001EJMS6K?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71w+qtq+PcL._AC_SL1500_.jpg"
        },
        {
            "name": "Yes4All Vinyl Coated Kettlebell Set",
            "price": "$69.99",
            "rating": "4.6",
            "url": "https://www.amazon.com/dp/B06XKDJ8C7?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71+CVnB1s+L._AC_SL1500_.jpg"
        },
        {
            "name": "BalanceFrom GoYoga All-Purpose Yoga Mat",
            "price": "$19.99",
            "rating": "4.5",
            "url": "https://www.amazon.com/dp/B01JFFEW3G?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71S+W2bQZFL._AC_SL1500_.jpg"
        }
    ],
    "camping-essentials-for-beginners": [
        {
            "name": "Coleman Sundome 4-Person Tent",
            "price": "$89.99",
            "rating": "4.6",
            "url": "https://www.amazon.com/dp/B004J2GUP4?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71rAmHHB+XL._AC_SL1500_.jpg"
        },
        {
            "name": "Teton Sports Celsius XXL Sleeping Bag",
            "price": "$89.99",
            "rating": "4.7",
            "url": "https://www.amazon.com/dp/B004EHDCHC?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71OzGs1FkLL._AC_SL1500_.jpg"
        },
        {
            "name": "Coleman Portable Propane Stove",
            "price": "$52.99",
            "rating": "4.7",
            "url": "https://www.amazon.com/dp/B00005OU9D?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71U+YGBf+L._AC_SL1500_.jpg"
        },
        {
            "name": "GearLight LED Headlamp Flashlight",
            "price": "$17.99",
            "rating": "4.6",
            "url": "https://www.amazon.com/dp/B07R5QD6M9?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71iOs3s-bhL._AC_SL1500_.jpg"
        },
        {
            "name": "First Aid Only 299 Piece First Aid Kit",
            "price": "$19.99",
            "rating": "4.7",
            "url": "https://www.amazon.com/dp/B000H5S7E0?tag=redikicks0c-20",
            "image": "https://m.media-amazon.com/images/I/71vK+Q-KM+L._AC_SL1500_.jpg"
        }
    ]
}

def generate_product_table(products):
    """Generate HTML product table"""
    rows = ""
    for product in products:
        stars = "⭐" * int(float(product['rating']))
        rows += f"""
    <tr>
      <td class="p-4 flex items-center gap-3">
        <img src="{product['image']}" alt="{product['name']}" class="w-16 h-16 object-contain rounded" />
        <span class="font-medium">{product['name']}</span>
      </td>
      <td class="p-4 text-accent font-bold">{product['price']}</td>
      <td class="p-4">{stars} ({product['rating']})</td>
      <td class="p-4">
        <a href="{product['url']}" target="_blank" rel="nofollow sponsored" class="inline-block bg-accent hover:bg-red-600 text-white px-4 py-2 rounded-lg text-sm font-semibold transition-colors">
          View on Amazon
        </a>
      </td>
    </tr>"""
    
    return f"""<!-- AMAZON PRODUCTS SECTION -->
<h3>Top Recommended Products</h3>
<p class="text-gray-400 mb-4">Based on our research, here are the best options available on Amazon. (As an Amazon Associate, we earn from qualifying purchases)</p>

<div class="overflow-x-auto my-8">
  <table class="w-full border-collapse bg-secondary/30 rounded-xl overflow-hidden">
    <thead>
      <tr class="bg-accent text-white">
        <th class="p-4 text-left">Product</th>
        <th class="p-4 text-left">Price</th>
        <th class="p-4 text-left">Rating</th>
        <th class="p-4 text-left">Link</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-white/10">
      {rows}
    </tbody>
  </table>
</div>

<div class="bg-secondary/20 border border-white/10 p-4 rounded-xl text-sm text-gray-400 mt-4">
  <strong>Disclaimer:</strong> Prices and availability are subject to change. We may earn a commission from purchases made through these links at no additional cost to you.
</div>
"""

def update_article(file_path, slug):
    """Update article with images and products"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace image placeholders with actual generated images
    for i in range(1, 4):
        old_path = f"{slug}-{i}.jpg"
        new_path = f"/redikicks-astro/images/{slug}-{i}.jpg"
        content = content.replace(old_path, new_path)
    
    # Add product table if products exist for this article
    if slug in amazon_products:
        product_section = generate_product_table(amazon_products[slug])
        
        # Insert before the conclusion section
        if '<h2 id="conclusion"' in content:
            content = content.replace(
                '<h2 id="conclusion"',
                f'{product_section}\n\n<h2 id="conclusion"'
            )
        else:
            # Add before the final div/section
            content = content.replace(
                '<!-- RELATED ARTICLES -->',
                f'{product_section}\n\n<!-- RELATED ARTICLES -->'
            )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated: {file_path}")

# Update all articles
articles_dir = "src/content/posts"
articles = [
    "best-affordable-mens-watches-under-100.md",
    "first-date-tips-for-men.md",
    "how-to-negotiate-salary-raise.md",
    "best-home-workout-equipment-for-men.md",
    "camping-essentials-for-beginners.md"
]

print("Updating articles with images and products...")
print("="*60)

for article in articles:
    slug = article.replace('.md', '')
    file_path = os.path.join(articles_dir, article)
    if os.path.exists(file_path):
        update_article(file_path, slug)
    else:
        print(f"❌ Not found: {file_path}")

print("="*60)
print("✅ All articles updated successfully!")
