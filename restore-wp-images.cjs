const fs = require('fs');
const path = require('path');

// Load all media to create ID -> URL mapping
const mediaFiles = fs.readdirSync('.').filter(f => f.startsWith('media-page-') && f.endsWith('.json'));
let allMedia = [];
mediaFiles.forEach(file => {
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  allMedia = allMedia.concat(data);
});

// Create mapping: media ID -> WordPress URL
const mediaUrlMap = {};
allMedia.forEach(item => {
  if (item.source_url) {
    mediaUrlMap[item.id] = item.source_url;
  }
});

console.log(`Created URL mapping for ${Object.keys(mediaUrlMap).length} media items`);

// Load all posts to get featured_media IDs
const postFiles = [];
for (let i = 1; i <= 9; i++) {
  const file = `posts-page-${i}.json`;
  if (fs.existsSync(file)) {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    postFiles.push(...data);
  }
}

// Create post slug -> featured_media mapping
const postMediaMap = {};
postFiles.forEach(post => {
  if (post.featured_media && post.featured_media !== 0) {
    postMediaMap[post.slug] = post.featured_media;
  }
});

console.log(`Found ${Object.keys(postMediaMap).length} posts with featured media`);

// Update all post files
const postsDir = 'src/content/posts';
const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));

let updated = 0;
let wordpressUrl = 0;

files.forEach((file, index) => {
  const filepath = path.join(postsDir, file);
  let content = fs.readFileSync(filepath, 'utf8');
  
  // Extract slug from filename
  const slug = file.replace('.md', '');
  
  // Get the featured_media ID for this post
  const mediaId = postMediaMap[slug];
  
  if (mediaId && mediaUrlMap[mediaId]) {
    // Update to use WordPress URL
    const wpUrl = mediaUrlMap[mediaId];
    content = content.replace(
      /featured_image:.*/,
      `featured_image: "${wpUrl}"`
    );
    wordpressUrl++;
  } else {
    // Set to null if no mapping
    content = content.replace(
      /featured_image:.*/,
      'featured_image: null'
    );
  }
  
  fs.writeFileSync(filepath, content);
  updated++;
  
  if ((index + 1) % 100 === 0) {
    console.log(`Updated ${index + 1} posts...`);
  }
});

console.log(`\n✅ Done! Updated ${updated} posts with WordPress URLs: ${wordpressUrl}`);
