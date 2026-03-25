const fs = require('fs');
const path = require('path');

// Read posts
const posts = JSON.parse(fs.readFileSync('posts.json', 'utf8'));
const categories = JSON.parse(fs.readFileSync('categories.json', 'utf8'));

// Create category map
const categoryMap = {};
categories.forEach(cat => {
  categoryMap[cat.id] = cat.name.replace(/&amp;/g, '&');
});

console.log(`Processing ${posts.length} posts...`);

posts.forEach((post, index) => {
  const slug = post.slug;
  const title = post.title.rendered.replace(/<[^>]+>/g, '');
  const content = post.content.rendered;
  const excerpt = post.excerpt.rendered.replace(/<[^>]+>/g, '').substring(0, 200);
  const date = post.date;
  const categoryIds = post.categories || [];
  const tagIds = post.tags || [];
  const featuredMedia = post.featured_media;
  
  const categoryNames = categoryIds.map(id => categoryMap[id] || 'Uncategorized');
  
  // Create markdown frontmatter
  const frontmatter = `---
title: "${title.replace(/"/g, '\\"')}"
slug: "${slug}"
date: "${date}"
categories: [${categoryNames.map(c => `"${c.replace(/"/g, '\\"')}"`).join(', ')}]
excerpt: "${excerpt.replace(/"/g, '\\"').replace(/\n/g, ' ')}"
featured_image: ${featuredMedia ? `"https://redikicks.com/wp-content/uploads/2025/03/featured_image_${post.id}.png"` : 'null'}
---

${content}
`;

  // Write file
  fs.writeFileSync(`src/content/posts/${slug}.md`, frontmatter);
  
  if ((index + 1) % 10 === 0) {
    console.log(`Processed ${index + 1} posts...`);
  }
});

console.log(`✅ Created ${posts.length} post files in src/content/posts/`);
