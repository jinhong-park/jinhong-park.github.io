---
layout: page
title: entire-collection
permalink: /entire-collection/
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

    <li class="listing-seperator"><p>{{ post.title }}</p></li>

  <li class="listing-item">
	  	{{ post.content }}
  </li>
  {% endif %}
{% endfor %}
</ul>
