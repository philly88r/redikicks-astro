const fs = require('fs');
const path = require('path');

// Load all media to create ID -> filename mapping
const mediaFiles = fs.readdirSync('.').filter(f => f.startsWith('media-page-') && f.endsWith('.json'));
let allMedia = [];
mediaFiles.forEach(file => {
  const data = JSON.parse(fs.readFileSync(file, 'utf8'));
  allMedia = allMedia.concat(data);
});

// Create mapping: media ID -> local filename
const mediaMap = {};
allMedia.forEach(item => {
  if (item.source_url) {
    const filename = path.basename(item.source_url);
    mediaMap[item.id] = filename;
  }
});

console.log(`Created mapping for ${Object.keys(mediaMap).length} media items`);

// Update all post files
const postsDir = 'src/content/posts';
const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));

console.log(`Updating ${files.length} posts with correct featured images...`);

let updated = 0;
let missing = 0;

files.forEach((file, index) => {
  const filepath = path.join(postsDir, file);
  let content = fs.readFileSync(filepath, 'utf8');
  
  // Extract frontmatter
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
  if (!frontmatterMatch) return;
  
  let frontmatter = frontmatterMatch[1];
  
  // Check if featured_image references a media ID that needs mapping
  const featuredMatch = frontmatter.match(/featured_image:\s*(.+)/);
  if (featuredMatch) {
    const currentValue = featuredMatch[1].trim();
    
    // If it's a local path with featured_image_ prefix, check if file exists
    if (currentValue.includes('featured_image_')) {
      const filename = currentValue.replace('/redikicks-astro/images/', '');
      if (!fs.existsSync(`public/images/${filename}`)) {
        // Try to find the media by extracting the post ID from the filename
        const postId = filename.match(/featured_image_(\d+)/)?.[1];
        if (postId && mediaMap[postId]) {
          // Update to use the correct filename
          frontmatter = frontmatter.replace(
            /featured_image:.*/,
            `featured_image: "/redikicks-astro/images/${mediaMap[postId]}"`
          );
          updated++;
        } else {
          // Set to null if no mapping found
          frontmatter = frontmatter.replace(
            /featured_image:.*/,
            'featured_image: null'
          );
          missing++;
        }
      }
    }
  }
  
  // Replace frontmatter in content
  content = content.replace(/^---\n[\s\S]*?\n---/, `---\n${frontmatter}\n---`);
  
  fs.writeFileSync(filepath, content);
  
  if ((index + 1) % 100 === 0) {
    console.log(`Processed ${index + 1} posts...`);
  }
});

console.log(`\n✅ Done! Updated: ${updated}, Set to null: ${missing}`);
