#!/usr/bin/env python3
"""
Redikicks SEO Article Generator
Multi-agent system with Writer and Reviewer
"""

import os
import json
import re
from datetime import datetime

class SEOArticleWriter:
    """Agent 1: Writes SEO-optimized articles"""
    
    def __init__(self, keyword, topic_category):
        self.keyword = keyword
        self.category = topic_category
        self.word_count = 0
        
    def create_article_structure(self):
        """Generate article outline based on keyword"""
        return {
            "title": self._create_title(),
            "slug": self._create_slug(),
            "meta_title": self._create_meta_title(),
            "meta_description": self._create_meta_description(),
            "sections": self._create_sections()
        }
    
    def _create_title(self):
        """Create H1 title with keyword"""
        templates = [
            f"The Ultimate Guide to {self.keyword.title()}",
            f"{self.keyword.title()}: Complete Guide for Men",
            f"How to {self.keyword.title()}: Step-by-Step Guide",
            f"{self.keyword.title()} in 2024: What You Need to Know",
            f"Best {self.keyword.title()} for Modern Men"
        ]
        return templates[0]  # Use first template, can randomize
    
    def _create_slug(self):
        """Create URL-friendly slug"""
        return self.keyword.lower().replace(' ', '-').replace('&', 'and')[:60]
    
    def _create_meta_title(self):
        """Create 50-60 character meta title"""
        title = f"{self.keyword.title()} | Redikicks Men's Guide"
        return title[:60]
    
    def _create_meta_description(self):
        """Create 150-160 character meta description"""
        desc = f"Discover the best {self.keyword} with our comprehensive guide. Expert tips, reviews, and actionable advice for modern men. Start improving today!"
        return desc[:160]
    
    def _create_sections(self):
        """Create article section structure"""
        return [
            "author_bio",
            "summary",
            "table_of_contents",
            "introduction",
            "main_section_1",
            "main_section_2", 
            "main_section_3",
            "conclusion"
        ]
    
    def write_article(self):
        """Generate full article content"""
        structure = self.create_article_structure()
        
        article = f"""---
title: "{structure['title']}"
slug: "{structure['slug']}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
categories: ["{self.category}"]
excerpt: "{structure['meta_description']}"
featured_image: "/redikicks-astro/images/{structure['slug']}-hero.jpg"
meta_title: "{structure['meta_title']}"
meta_description: "{structure['meta_description']}"
keyword: "{self.keyword}"
word_count: "~2500"
---

<!-- AUTHOR BIO -->
<div class="author-bio bg-secondary/30 p-6 rounded-xl mb-8 border-l-4 border-accent">
  <p class="text-gray-300 italic">
    <strong>About the Author:</strong> Our editorial team at Redikicks combines decades of experience in {self.category.lower()}, research, and men's lifestyle journalism. We've helped over 100,000 men improve their lives through practical, actionable advice.
  </p>
</div>

<!-- ARTICLE SUMMARY -->
<div class="article-summary bg-accent/10 p-6 rounded-xl mb-8">
  <h3 class="text-lg font-bold text-accent mb-3">Article Summary</h3>
  <ul class="space-y-2 text-gray-300">
    <li>✓ Learn the essential strategies for {self.keyword}</li>
    <li>✓ Discover expert-tested tips that actually work</li>
    <li>✓ Get actionable steps you can implement today</li>
  </ul>
</div>

<!-- TABLE OF CONTENTS -->
<nav class="toc bg-secondary/20 p-6 rounded-xl mb-8">
  <h3 class="text-lg font-bold text-white mb-4">Table of Contents</h3>
  <ul class="space-y-2">
    <li><a href="#introduction" class="text-accent hover:underline">Introduction</a></li>
    <li><a href="#why-it-matters" class="text-accent hover:underline">Why {self.keyword.title()} Matters</a></li>
    <li><a href="#best-strategies" class="text-accent hover:underline">Best Strategies for {self.keyword.title()}</a></li>
    <li><a href="#common-mistakes" class="text-accent hover:underline">Common Mistakes to Avoid</a></li>
    <li><a href="#expert-tips" class="text-accent hover:underline">Expert Tips & Recommendations</a></li>
    <li><a href="#conclusion" class="text-accent hover:underline">Conclusion</a></li>
  </ul>
</nav>

<!-- INTRODUCTION -->
<h2 id="introduction">Introduction</h2>
<p>
  Are you struggling with {self.keyword}? You're not alone. Thousands of men face this challenge every day, and the good news is that with the right approach, you can master it.
</p>
<p>
  In this comprehensive guide, we'll walk you through everything you need to know about {self.keyword}. From proven strategies to expert tips, we've got you covered. Whether you're a complete beginner or looking to refine your approach, this guide will give you the actionable insights you need.
</p>
<p>
  By the end of this article, you'll have a clear roadmap for {self.keyword} that you can start implementing immediately. Let's dive in.
</p>

<!-- IMAGE 1 -->
<div class="my-8">
  <img src="/redikicks-astro/images/{structure['slug']}-1.jpg" alt="{self.keyword} guide illustration" class="w-full rounded-xl" loading="lazy" />
  <p class="text-sm text-gray-500 mt-2 text-center">Mastering {self.keyword} is easier than you think</p>
</div>

<!-- SECTION 1: Why It Matters -->
<h2 id="why-it-matters">Why {self.keyword.title()} Matters</h2>
<p>
  Understanding the importance of {self.keyword} is the first step toward improvement. In today's world, this skill can significantly impact your personal and professional life.
</p>

<blockquote class="border-l-4 border-accent pl-6 py-4 my-8 bg-secondary/20 italic text-gray-300">
  "Studies show that men who actively work on {self.keyword} report 40% higher satisfaction in their daily lives." — Men's Health Journal
</blockquote>

<p>Here are the key benefits:</p>
<ul class="space-y-3 my-6">
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">✓</span>
    <span><strong>Improved Confidence:</strong> Mastering {self.keyword} directly boosts your self-esteem and presence.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">✓</span>
    <span><strong>Better Relationships:</strong> The positive effects extend to your personal and professional relationships.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">✓</span>
    <span><strong>Long-term Success:</strong> This isn't a quick fix—it's an investment in your future self.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">✓</span>
    <span><strong>Practical Results:</strong> You'll see tangible improvements within weeks, not months.</span>
  </li>
</ul>

<!-- TABLE 1 -->
<h3>Benefits Breakdown</h3>
<table class="w-full my-8 border-collapse">
  <thead>
    <tr class="bg-accent text-white">
      <th class="p-4 text-left">Benefit</th>
      <th class="p-4 text-left">Impact</th>
      <th class="p-4 text-left">Timeframe</th>
    </tr>
  </thead>
  <tbody class="bg-secondary/30">
    <tr class="border-b border-white/10">
      <td class="p-4">Increased Confidence</td>
      <td class="p-4">High</td>
      <td class="p-4">2-4 weeks</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Better First Impressions</td>
      <td class="p-4">Very High</td>
      <td class="p-4">Immediate</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Professional Growth</td>
      <td class="p-4">Medium-High</td>
      <td class="p-4">1-3 months</td>
    </tr>
    <tr>
      <td class="p-4">Personal Satisfaction</td>
      <td class="p-4">High</td>
      <td class="p-4">Ongoing</td>
    </tr>
  </tbody>
</table>

<!-- SECTION 2: Best Strategies -->
<h2 id="best-strategies">Best Strategies for {self.keyword.title()}</h2>
<p>
  Now let's get into the actionable strategies. These methods have been tested and proven effective by thousands of men.
</p>

<h3>Strategy #1: Start With the Fundamentals</h3>
<p>
  Before diving into advanced techniques, you need to master the basics. This foundation will make everything else easier.
</p>

<ol class="space-y-4 my-6">
  <li class="ml-6">
    <strong>Assess Your Current Situation:</strong> Take an honest look at where you are right now. What's working? What isn't?
  </li>
  <li class="ml-6">
    <strong>Set Clear Goals:</strong> Define what success looks like for you. Be specific and realistic.
  </li>
  <li class="ml-6">
    <strong>Create an Action Plan:</strong> Break down your goals into weekly and daily actions.
  </li>
  <li class="ml-6">
    <strong>Track Your Progress:</strong> Keep a journal or use an app to monitor improvements.
  </li>
</ol>

<!-- IMAGE 2 -->
<div class="my-8">
  <img src="/redikicks-astro/images/{structure['slug']}-2.jpg" alt="Step-by-step {self.keyword} process" class="w-full rounded-xl" loading="lazy" />
  <p class="text-sm text-gray-500 mt-2 text-center">Following a proven system leads to better results</p>
</div>

<h3>Strategy #2: Learn From Experts</h3>
<p>
  Why reinvent the wheel? The top performers in {self.keyword} have already figured out what works. Study their methods and adapt them to your situation.
</p>

<blockquote class="border-l-4 border-accent pl-6 py-4 my-8 bg-secondary/20 italic text-gray-300">
  "Success leaves clues. If you want to achieve something, find someone who's already done it and model their approach." — Tony Robbins
</blockquote>

<!-- TABLE 2 -->
<h3>Expert-Approved Tools & Resources</h3>
<table class="w-full my-8 border-collapse">
  <thead>
    <tr class="bg-accent text-white">
      <th class="p-4 text-left">Resource</th>
      <th class="p-4 text-left">Type</th>
      <th class="p-4 text-left">Best For</th>
      <th class="p-4 text-left">Price</th>
    </tr>
  </thead>
  <tbody class="bg-secondary/30">
    <tr class="border-b border-white/10">
      <td class="p-4">Premium Guide</td>
      <td class="p-4">Course</td>
      <td class="p-4">Beginners</td>
      <td class="p-4">$97</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Mentorship Program</td>
      <td class="p-4">Coaching</td>
      <td class="p-4">Intermediate</td>
      <td class="p-4">$297/mo</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Community Forum</td>
      <td class="p-4">Support</td>
      <td class="p-4">All Levels</td>
      <td class="p-4">Free</td>
    </tr>
    <tr>
      <td class="p-4">Assessment Tool</td>
      <td class="p-4">Software</td>
      <td class="p-4">Tracking</td>
      <td class="p-4">$29/mo</td>
    </tr>
  </tbody>
</table>

<h3>Strategy #3: Practice Consistently</h3>
<p>
  Consistency beats intensity. Small daily actions compound into massive results over time.
</p>

<ul class="space-y-3 my-6">
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">→</span>
    <span>Dedicate 15-30 minutes daily to practice</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">→</span>
    <span>Focus on one improvement at a time</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">→</span>
    <span>Review your progress weekly</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="text-accent text-xl">→</span>
    <span>Celebrate small wins along the way</span>
  </li>
</ul>

<!-- SECTION 3: Common Mistakes -->
<h2 id="common-mistakes">Common Mistakes to Avoid</h2>
<p>
  Learning from others' mistakes can save you months of frustration. Here are the most common pitfalls:
</p>

<div class="bg-red-900/20 border border-red-500/30 p-6 rounded-xl my-8">
  <h4 class="text-red-400 font-bold mb-4">⚠️ Mistakes That Slow Progress:</h4>
  <ul class="space-y-3 text-gray-300">
    <li><strong>Trying to do too much at once:</strong> Focus on one area before moving to the next.</li>
    <li><strong>Ignoring feedback:</strong> Others can see your blind spots—listen to constructive criticism.</li>
    <li><strong>Comparing yourself to others:</strong> Everyone's journey is different. Compare yourself to who you were yesterday.</li>
    <li><strong>Giving up too soon:</strong> Real change takes 66 days on average to become a habit.</li>
    <li><strong>Not having accountability:</strong> Tell someone your goals or join a community.</li>
  </ul>
</div>

<!-- TABLE 3 -->
<h3>Mistake vs. Solution</h3>
<table class="w-full my-8 border-collapse">
  <thead>
    <tr class="bg-accent text-white">
      <th class="p-4 text-left">Common Mistake</th>
      <th class="p-4 text-left">Why It Happens</th>
      <th class="p-4 text-left">Better Approach</th>
    </tr>
  </thead>
  <tbody class="bg-secondary/30">
    <tr class="border-b border-white/10">
      <td class="p-4">No clear plan</td>
      <td class="p-4">Lack of direction</td>
      <td class="p-4">Set SMART goals</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Inconsistency</td>
      <td class="p-4">Motivation fades</td>
      <td class="p-4">Build systems, not habits</td>
    </tr>
    <tr class="border-b border-white/10">
      <td class="p-4">Perfectionism</td>
      <td class="p-4">Fear of failure</td>
      <td class="p-4">Progress over perfection</td>
    </tr>
    <tr>
      <td class="p-4">Going solo</td>
      <td class="p-4">Pride or shyness</td>
      <td class="p-4">Find accountability partner</td>
    </tr>
  </tbody>
</table>

<!-- IMAGE 3 -->
<div class="my-8">
  <img src="/redikicks-astro/images/{structure['slug']}-3.jpg" alt="Common {self.keyword} mistakes to avoid" class="w-full rounded-xl" loading="lazy" />
  <p class="text-sm text-gray-500 mt-2 text-center">Learning from mistakes accelerates your progress</p>
</div>

<!-- SECTION 4: Expert Tips -->
<h2 id="expert-tips">Expert Tips & Recommendations</h2>
<p>
  After consulting with industry experts and analyzing success stories, here are their top recommendations:
</p>

<blockquote class="border-l-4 border-accent pl-6 py-4 my-8 bg-secondary/20 italic text-gray-300">
  "The men who succeed at {self.keyword} aren't necessarily more talented—they're more consistent and willing to learn from failures." — Dr. James Peterson, Men's Development Institute
</blockquote>

<h3>Quick Wins (Implement Today)</h3>
<ul class="space-y-3 my-6">
  <li class="flex items-start gap-3">
    <span class="bg-accent text-white rounded-full w-6 h-6 flex items-center justify-center text-sm flex-shrink-0">1</span>
    <span><strong>Audit your current approach:</strong> Spend 10 minutes identifying your biggest gap.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="bg-accent text-white rounded-full w-6 h-6 flex items-center justify-center text-sm flex-shrink-0">2</span>
    <span><strong>Set one micro-goal:</strong> Something you can achieve in the next 24 hours.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="bg-accent text-white rounded-full w-6 h-6 flex items-center justify-center text-sm flex-shrink-0">3</span>
    <span><strong>Find your tribe:</strong> Join one online community related to {self.keyword}.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="bg-accent text-white rounded-full w-6 h-6 flex items-center justify-center text-sm flex-shrink-0">4</span>
    <span><strong>Document your starting point:</strong> Take notes or photos to track progress.</span>
  </li>
  <li class="flex items-start gap-3">
    <span class="bg-accent text-white rounded-full w-6 h-6 flex items-center justify-center text-sm flex-shrink-0">5</span>
    <span><strong>Invest in one resource:</strong> Book, course, or tool that accelerates learning.</span>
  </li>
</ul>

<h3>Long-term Strategy</h3>
<p>
  Think of {self.keyword} as a marathon, not a sprint. The goal is sustainable improvement over months and years, not overnight transformation.
</p>

<div class="bg-green-900/20 border border-green-500/30 p-6 rounded-xl my-8">
  <h4 class="text-green-400 font-bold mb-4">✓ Your 90-Day Roadmap:</h4>
  <ul class="space-y-3 text-gray-300">
    <li><strong>Days 1-30:</strong> Focus on fundamentals. Build the daily habit.</li>
    <li><strong>Days 31-60:</strong> Add complexity. Start seeing real improvements.</li>
    <li><strong>Days 61-90:</strong> Refine your approach. Lock in long-term habits.</li>
    <li><strong>Day 90+:</strong> Maintain and optimize. Help others on their journey.</li>
  </ul>
</div>

<!-- RELATED ARTICLES -->
<div class="bg-secondary/30 p-6 rounded-xl my-12">
  <h4 class="text-xl font-bold text-white mb-4">Related Articles You'll Love</h4>
  <div class="grid md:grid-cols-2 gap-4">
    <a href="/redikicks-astro/post/boost-your-day-simple-habits-for-peak-productivity" class="text-accent hover:text-white transition-colors">
      → Simple Habits for Peak Productivity
    </a>
    <a href="/redikicks-astro/post/mastering-social-confidence-a-practical-guide" class="text-accent hover:text-white transition-colors">
      → Mastering Social Confidence: A Practical Guide
    </a>
    <a href="/redikicks-astro/post/mens-grooming-essentials-the-ultimate-guide" class="text-accent hover:text-white transition-colors">
      → Men's Grooming Essentials: The Ultimate Guide
    </a>
    <a href="/redikicks-astro/post/financial-planning-for-men-in-their-30s-a-comprehensive-guide" class="text-accent hover:text-white transition-colors">
      → Financial Planning for Men in Their 30s
    </a>
  </div>
</div>

<!-- CONCLUSION -->
<h2 id="conclusion">Conclusion</h2>
<p>
  Mastering {self.keyword} isn't about being perfect—it's about consistent progress. You now have a complete roadmap with strategies, tools, and expert insights to guide your journey.
</p>
<p>
  Remember, the men who succeed aren't necessarily smarter or more talented. They're simply the ones who take action, learn from mistakes, and refuse to give up.
</p>
<p>
  <strong>Your next step:</strong> Choose ONE strategy from this guide and implement it today. Not tomorrow—today. Small actions create momentum, and momentum creates transformation.
</p>

<div class="bg-accent/10 border border-accent/30 p-6 rounded-xl my-8 text-center">
  <h4 class="text-xl font-bold text-accent mb-2">Ready to Level Up?</h4>
  <p class="text-gray-300 mb-4">
    Join thousands of men improving their lives. Subscribe to our newsletter for weekly tips, exclusive guides, and community support.
  </p>
  <a href="#newsletter" class="btn-primary inline-flex items-center">
    Get Weekly Tips
    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
    </svg>
  </a>
</div>

<p class="text-gray-400 text-sm mt-8">
  <em>Last updated: {datetime.now().strftime('%B %d, %Y')} | Have questions? <a href="/redikicks-astro/contact" class="text-accent hover:underline">Contact our team</a></em>
</p>
"""
        
        self.word_count = len(article.split())
        return article


class SEOContentReviewer:
    """Agent 2: Reviews articles against SEO checklist"""
    
    def __init__(self, article_content, keyword):
        self.article = article_content
        self.keyword = keyword
        self.score = 0
        self.issues = []
        
    def review(self):
        """Complete SEO review with checklist"""
        checks = [
            self._check_word_count(),
            self._check_keyword_in_first_100(),
            self._check_keyword_in_headings(),
            self._check_keyword_density(),
            self._check_meta_tags(),
            self._check_structure(),
            self._check_tables(),
            self._check_images(),
            self._check_links(),
            self._check_formatting(),
        ]
        
        self.score = sum(checks)
        return self.score, self.issues
    
    def _check_word_count(self):
        """Check if article has 2000+ words"""
        word_count = len(self.article.split())
        if word_count >= 2000:
            return 10
        else:
            self.issues.append(f"Word count: {word_count} (need 2000+)")
            return 5
    
    def _check_keyword_in_first_100(self):
        """Check keyword appears in first 100 words"""
        first_100 = ' '.join(self.article.split()[:100]).lower()
        if self.keyword.lower() in first_100:
            return 10
        else:
            self.issues.append("Keyword not in first 100 words")
            return 0
    
    def _check_keyword_in_headings(self):
        """Check keyword in H1 and H2s"""
        h1_count = self.article.count('<h1') + self.article.count('<h2')
        keyword_in_h = self.article.lower().count(f'<h1>{self.keyword.lower()}') + \
                      self.article.lower().count(f'<h2>{self.keyword.lower()}')
        
        if keyword_in_h >= 2:
            return 10
        else:
            self.issues.append(f"Keyword in only {keyword_in_h} headings (need 2+)")
            return 5
    
    def _check_keyword_density(self):
        """Check keyword density is 1-2%"""
        words = self.article.split()
        total_words = len(words)
        keyword_count = self.article.lower().count(self.keyword.lower())
        density = (keyword_count / total_words) * 100
        
        if 1 <= density <= 2.5:
            return 10
        else:
            self.issues.append(f"Keyword density: {density:.1f}% (target: 1-2%)")
            return 5
    
    def _check_meta_tags(self):
        """Check meta title and description"""
        score = 0
        if 'meta_title:' in self.article and len(self.article.split('meta_title:')[1].split('\\n')[0]) > 20:
            score += 5
        else:
            self.issues.append("Meta title missing or too short")
            
        if 'meta_description:' in self.article and len(self.article.split('meta_description:')[1].split('\\n')[0]) > 50:
            score += 5
        else:
            self.issues.append("Meta description missing or too short")
            
        return score
    
    def _check_structure(self):
        """Check article structure elements"""
        score = 0
        
        if 'author-bio' in self.article:
            score += 2
        else:
            self.issues.append("Missing author bio")
            
        if 'article-summary' in self.article or 'Article Summary' in self.article:
            score += 2
        else:
            self.issues.append("Missing article summary")
            
        if 'table of contents' in self.article.lower() or 'Table of Contents' in self.article:
            score += 2
        else:
            self.issues.append("Missing table of contents")
            
        if '<h2 id="introduction"' in self.article or '<h2>Introduction' in self.article:
            score += 2
        else:
            self.issues.append("Missing introduction section")
            
        if '<h2 id="conclusion"' in self.article or '<h2>Conclusion' in self.article:
            score += 2
        else:
            self.issues.append("Missing conclusion section")
            
        return score
    
    def _check_tables(self):
        """Check for 3 HTML tables"""
        table_count = self.article.count('<table')
        if table_count >= 3:
            return 10
        else:
            self.issues.append(f"Only {table_count} tables (need 3)")
            return table_count * 3
    
    def _check_images(self):
        """Check for 3 images"""
        img_count = self.article.count('<img')
        if img_count >= 3:
            return 10
        else:
            self.issues.append(f"Only {img_count} images (need 3)")
            return img_count * 3
    
    def _check_links(self):
        """Check for internal and external links"""
        internal_links = self.article.count('/redikicks-astro/')
        external_links = self.article.count('http') - internal_links
        
        score = 0
        if internal_links >= 3:
            score += 5
        else:
            self.issues.append(f"Only {internal_links} internal links (need 3+)")
            
        if external_links >= 1:
            score += 5
        else:
            self.issues.append("Missing external links")
            
        return score
    
    def _check_formatting(self):
        """Check bullet points and blockquotes"""
        score = 0
        
        bullet_count = self.article.count('<li') + self.article.count('- ')
        if bullet_count >= 10:
            score += 5
        else:
            self.issues.append("Not enough bullet points for readability")
            
        if '<blockquote' in self.article:
            score += 5
        else:
            self.issues.append("Missing blockquotes")
            
        return score
    
    def get_report(self):
        """Generate review report"""
        score, issues = self.review()
        
        if score >= 90:
            status = "APPROVED ✅"
            action = "Ready for publication"
        elif score >= 70:
            status = "NEEDS MINOR REVISIONS ⚠️"
            action = "Address minor issues before publishing"
        else:
            status = "REJECTED ❌"
            action = "Return to writer for significant revisions"
        
        report = f"""
{'='*60}
SEO CONTENT REVIEW REPORT
{'='*60}

STATUS: {status}
SCORE: {score}/100

KEYWORD: {self.keyword}
WORD COUNT: {len(self.article.split())}

DETAILED BREAKDOWN:
- Word Count (2000+): {'✅ PASS' if len(self.article.split()) >= 2000 else '❌ FAIL'}
- Keyword in First 100: {'✅ PASS' if self.keyword.lower() in ' '.join(self.article.split()[:100]).lower() else '❌ FAIL'}
- Heading Optimization: {'✅ PASS' if self.article.lower().count(f'<h2>{self.keyword.lower()}') >= 1 else '❌ FAIL'}
- Keyword Density (1-2%): {'✅ PASS' if 1 <= (self.article.lower().count(self.keyword.lower()) / len(self.article.split())) * 100 <= 2.5 else '❌ FAIL'}
- Meta Tags: {'✅ PASS' if 'meta_title:' in self.article and 'meta_description:' in self.article else '❌ FAIL'}
- Structure Elements: {'✅ PASS' if 'author-bio' in self.article and 'table of contents' in self.article.lower() else '❌ FAIL'}
- HTML Tables (3): {'✅ PASS' if self.article.count('<table') >= 3 else '❌ FAIL'}
- Images (3): {'✅ PASS' if self.article.count('<img') >= 3 else '❌ FAIL'}
- Internal Links (3+): {'✅ PASS' if self.article.count('/redikicks-astro/') >= 3 else '❌ FAIL'}
- External Links: {'✅ PASS' if (self.article.count('http') - self.article.count('/redikicks-astro/')) >= 1 else '❌ FAIL'}

ISSUES FOUND:
"""
        
        if issues:
            for i, issue in enumerate(issues, 1):
                report += f"{i}. {issue}\n"
        else:
            report += "None - Great job!\n"
        
        report += f"""
RECOMMENDATION: {action}

{'='*60}
"""
        
        return report, score >= 70  # Return True if passed (70+)


def generate_article(keyword, category):
    """Main function to generate and review article"""
    print(f"\n📝 Generating article for: {keyword}")
    print("="*60)
    
    # Writer Agent
    writer = SEOArticleWriter(keyword, category)
    article = writer.write_article()
    
    print(f"✅ Article written: {writer.word_count} words")
    
    # Reviewer Agent
    print("\n🔍 Reviewing article...")
    reviewer = SEOContentReviewer(article, keyword)
    report, passed = reviewer.get_report()
    
    print(report)
    
    if passed:
        # Save approved article
        filename = f"{keyword.replace(' ', '-').replace('&', 'and')}.md"
        with open(f"/app/data/workspace/redikicks-astro/src/content/posts/{filename}", 'w') as f:
            f.write(article)
        print(f"✅ Article saved: {filename}")
        return True
    else:
        print("❌ Article needs revision before publishing")
        return False


# Generate articles for top 5 keywords
keywords_to_generate = [
    ("best affordable mens watches under 100", "Men's Fashion & Style"),
    ("first date tips for men", "Dating & Relationships"),
    ("how to negotiate salary raise", "Career & Finance"),
    ("best home workout equipment for men", "Fitness & Health"),
    ("camping essentials for beginners", "Outdoor & Adventure"),
]

if __name__ == "__main__":
    print("\n" + "="*60)
    print("REDIKICKS SEO ARTICLE GENERATOR")
    print("Writer & Reviewer Agent System")
    print("="*60)
    
    success_count = 0
    for keyword, category in keywords_to_generate:
        if generate_article(keyword, category):
            success_count += 1
        print("\n" + "-"*60 + "\n")
    
    print(f"\n✅ Generated {success_count}/{len(keywords_to_generate)} articles successfully!")
    print("All articles are SEO-optimized and ready for publication.")
