---
layout: page
title: fulllist
permalink: /fulllist/
---


<ul class="listing">

{% for post in site.posts %}

{% if post.title == "wjwkdth" %}

  <li class="listing-item">
	  	{{ post.content }}
  </li>
{% endif %}
   
{% endfor %}


{% for post in site.posts %}

{% if post.title != "wjwkdth" %}

    <li class="listing-seperator">{{ post.title }}</li>

  <li class="listing-item">
	  	{{ post.content }}
  </li>
  {% endif %}
{% endfor %}
</ul>
