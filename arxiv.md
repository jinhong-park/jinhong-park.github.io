---
layout: page
title: Arxiv
permalink: /arxiv/
---
 
  <a href="../../entire-collection"><b>   Entire collection  </b></a>
  <br>
  <b>  Sub-collections </b>
  <br>

  <table>
    <tr>
        <td><a href="../arxiv/altermagnet">Altermagnets</a></td>
        <td><a href="../arxiv/flat">Flat</a></td>
        <td><a href="../arxiv/hedgehog">Hedgehog</a></td>
        <td><a href="../arxiv/kagome">Kagome</a></td>
        <td><a href="../arxiv/kondo">Kondo</a></td>
        <td><a href="../arxiv/magnon">Magnon</a></td>
    </tr>
    <tr>
        <td><a href="../arxiv/majorana">Majorana</a></td>
        <td><a href="../arxiv/skyrmion">Skyrmion</a></td>
        <td><a href="../arxiv/spin">Spin</a></td>
        <td><a href="../arxiv/theory">Theory</a></td>
        <td><a href="../arxiv/wave">Wave</a></td>
        <td></td>
    </tr>
</table>
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
