---
layout: page
title: recent
permalink: /blog/recent
---
 
 <ul class="listing">

<a href="https://t.me/s/jinhong_park"><b>Daily Shorts</b></a> 

 {% for post in site.posts %}



<li class="listing-seperator"><p>{{ post.title }}</p></li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
