---
layout: page
title: recent
permalink: /blog/recent
---
 
 <ul class="listing">

 {% for post in site.posts %}



<li class="listing-seperator">{{ post.title }}</li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
