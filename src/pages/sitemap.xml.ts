import type { APIRoute } from 'astro';

export const GET: APIRoute = async () => {
  const baseUrl = 'https://philly88r.github.io/redikicks-astro';
  
  // Get all posts
  const posts = Object.values(import.meta.glob('../content/posts/*.md', { eager: true }));
  
  // Generate sitemap entries for posts
  const postEntries = posts.map((post: any) => ({
    url: `${baseUrl}/post/${post.frontmatter.slug}`,
    lastmod: post.frontmatter.date,
    changefreq: 'monthly',
    priority: '0.8'
  }));
  
  // Static pages
  const staticPages = [
    { url: `${baseUrl}/`, lastmod: new Date().toISOString(), changefreq: 'daily', priority: '1.0' },
    { url: `${baseUrl}/all-posts`, lastmod: new Date().toISOString(), changefreq: 'daily', priority: '0.9' },
    { url: `${baseUrl}/category/mens-fashion`, lastmod: new Date().toISOString(), changefreq: 'weekly', priority: '0.8' },
    { url: `${baseUrl}/category/fitness`, lastmod: new Date().toISOString(), changefreq: 'weekly', priority: '0.8' },
    { url: `${baseUrl}/category/dating-relationships`, lastmod: new Date().toISOString(), changefreq: 'weekly', priority: '0.8' },
    { url: `${baseUrl}/category/career-advice`, lastmod: new Date().toISOString(), changefreq: 'weekly', priority: '0.8' },
    { url: `${baseUrl}/category/outdoor-adventures`, lastmod: new Date().toISOString(), changefreq: 'weekly', priority: '0.8' },
  ];
  
  const allEntries = [...staticPages, ...postEntries];
  
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allEntries.map(entry => `  <url>
    <loc>${entry.url}</loc>
    <lastmod>${entry.lastmod}</lastmod>
    <changefreq>${entry.changefreq}</changefreq>
    <priority>${entry.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

  return new Response(sitemap, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600'
    }
  });
};
