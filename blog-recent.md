---
layout: page
title: recent
permalink: /blog/recent
---
 
 <ul class="listing">

<a href="https://t.me/s/jin_hongpark"> Daily Shorts </a>
<br>
<a href="https://ui.adsabs.harvard.edu"> Good Luck Search using Adsabs  </a>
<br>
<a href="https://scholar.google.com/"> google scholar </a>

 {% for post in site.posts %}



<li class="listing-seperator"><p>{{ post.title }}</p></li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
