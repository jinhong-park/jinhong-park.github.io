---
layout: page
title: recent
permalink: /blog/recent
---
 
 <ul class="listing">

[Daily Shorts](https://t.me/s/jinhong_park)

 {% for post in site.posts %}



<li class="listing-seperator"><p>{{ post.title }}</p></li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
