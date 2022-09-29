---
layout: page
title: fulllist
permalink: /fulllist/
---


<ul class="listing">


<a href="https://t.me/s/jinhong_park"><b>Daily Shorts</b></a>

{% for post in site.posts %}

{% if post.title == "wjwkdth" %}

  <li class="listing-item">
	  	{{ post.content }}
  </li>
{% endif %}
   
{% endfor %}


{% for post in site.posts %}

{% if post.title != "wjwkdth" %}

    <li class="listing-seperator"><p>{{ post.title }}</p></li>

  <li class="listing-item">
	  	{{ post.content }}
  </li>
  {% endif %}
{% endfor %}
</ul>
