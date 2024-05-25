---
layout: page
title: recent
permalink: /arxiv/recent
---
 
 <ul class="listing">


<a href="https://jinhong-park.github.io/t_me"> Daily t.me </a> 
<br>
<a href="#" onclick="window.open('https://ui.adsabs.harvard.edu', '_blank', 'width=1000,height=600');"> Good Luck Search using Adsabs </a>
<br>
<a href="#" onclick="window.open('https://scholar.google.com', '_blank', 'width=1000,height=600');"> google scholar </a>
<br>
<a href="#" onclick="window.open('https://typeset.io', '_blank', 'width=1000,height=600');"> typeset.io </a>


 {% for post in site.posts %}

<li class="listing-seperator"><p>{{ post.title }}</p></li>

   <li class="listing-item">
           {{ post.content }}
   </li>
    
    {% break %}
    
 {% endfor %}
 </ul>
  
