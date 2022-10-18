---
layout: page
title: recent
permalink: /blog/recent
---
 
 <ul class="listing">

<a href="https://t.me/s/jin_hongpark"> Daily Shorts </a>

  <a href="https://ui.adsabs.harvard.edu"> <b>Good Luck Search using Adsabs </b> </a>

 {% for post in site.posts %}



<li class="listing-seperator"><p>{{ post.title }}</p></li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
