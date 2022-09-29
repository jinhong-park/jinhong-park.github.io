---
layout: page
title: Blog
permalink: /blog/
---
 
  <a href="../../fulllist"><b>   Full list</b></a> 
  
  <a href="../blog/recent"><b>   recent </b></a> 
   
  <a href="https://t.me/s/jinhong_park"><b>Daily Shorts</b> </a>
   
<ul class="listing">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator"><p>{{ y }}</p></li>
  {% endif %}
  <li class="listing-item">
 <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time> 
    <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>

{% endfor %}
</ul>
