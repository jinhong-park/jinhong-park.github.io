---
layout: page
title: Arxiv
permalink: /arxiv/
---
 
  <a href="../../entire-collection"><b>   Entire collection  </b></a>
  <br>
  <b>  Sub-collection </b>
  <br>
  <a href="../arxiv/altermagnet">   Altermagnets  </a> &nbsp;<a href="../arxiv/spin">   Spin  </a> &nbsp;<a href="../arxiv/magnon">   Magnon  </a> &nbsp;<a href="../arxiv/skyrmion">   Skyrmion  </a> &nbsp;<a href="../arxiv/hedgehog">   Hedgehog  </a> &nbsp;<a href="../arxiv/flat">   Flat  </a>  &nbsp;<a href="../arxiv/majorana">   Majorana  </a>
  <br>
  <a href="../arxiv/recent"><b>   recent </b></a>
  <br>
  <a href="https://jinhong-park.github.io/t_me"><b> Daily t.me </b></a>
  <br>
  <a href="#" onclick="window.open('https://ui.adsabs.harvard.edu', '_blank', 'width=1000,height=600');"> Good Luck Search using Adsabs </a>
  <br>
  <a href="#" onclick="window.open('https://scholar.google.com', '_blank', 'width=1000,height=600');"> google scholar </a>
  <br>
  <a href="#" onclick="window.open('https://typeset.io', '_blank', 'width=1000,height=600');"> typeset.io </a>

   

   
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
