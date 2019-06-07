---
layout: page
title: fulllist
permalink: /fulllist/
---


<ul class="listing">
{% for post in site.posts %}


    <li class="listing-seperator">{{ post.title }}</li>

  <li class="listing-item">
	  	{{ post.content }}
  </li>
{% endfor %}
</ul>
