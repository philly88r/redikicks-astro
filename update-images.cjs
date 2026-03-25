const fs = require('fs');
const path = require('path');

// Read the media mapping
const media = JSON.parse(fs.readFileSync('all-media.json', 'utf8'));

// Create URL to local filename mapping
const urlMap = {};
media.forEach(item => {
  if (item.source_url) {
    const filename = path.basename(item.source_url).replace(/[^a-zA-Z0-9._-]/g, '_');
    urlMap[item.source_url] = `/redikicks-astro/images/${filename}`;
    // Also map without domain
    const urlPath = item.source_url.replace('https://redikicks.com', '');
    urlMap[urlPath] = `/redikicks-astro/images/${filename}`;
  }
});

console.log(`Created mapping for ${Object.keys(urlMap).length} URLs`);

// Update all post files
const postsDir = 'src/content/posts';
const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));

console.log(`Updating ${files.length} posts...`);

files.forEach((file, index) => {
  const filepath = path.join(postsDir, file);
  let content = fs.readFileSync(filepath, 'utf8');
  
  // Replace WordPress image URLs with local paths
  Object.keys(urlMap).forEach(wpUrl => {
    const localPath = urlMap[wpUrl];
    // Replace full URL
    content = content.split(wpUrl).join(localPath);
    // Replace URL-encoded version
    const encodedUrl = wpUrl.replace(/ /g, '%20');
    content = content.split(encodedUrl).join(localPath);
  });
  
  // Also fix any remaining redikicks.com/wp-content/uploads URLs
  content = content.replace(/https:\/\/redikicks\.com\/wp-content\/uploads\/[^\s")]+/g, (match) => {
    const filename = path.basename(match).replace(/[^a-zA-Z0-9._-]/g, '_');
    return `/redikicks-astro/images/${filename}`;
  });
  
  fs.writeFileSync(filepath, content);
  
  if ((index + 1) % 100 === 0) {
    console.log(`Updated ${index + 1} posts...`);
  }
});

console.log('✅ All posts updated with local image paths!');
