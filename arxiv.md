---
layout: page
title: Arxiv
permalink: /arxiv/
---
 
  <a href="../../entire-collection"><b>   Entire collection  </b></a>
  <br>
  
  <table>
      <tr>
        <th>Sub-collections</th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
    </tr>
    <tr>
        <th><a href="../arxiv/altermagnet">Altermagnets</a></th>
        <th><a href="../arxiv/cuprate">Cuprate</a></th>
        <th><a href="../arxiv/fege">FeGe</a></th>
        <th><a href="../arxiv/flat">Flatband</a></th>
        <th><a href="../arxiv/hedgehog">Hedgehog</a></th>
    </tr>
    <tr>
        <th><a href="../arxiv/iridate">Iridate</a></th>
        <th><a href="../arxiv/kagome">Kagome</a></th>
        <th><a href="../arxiv/kondo">Kondo</a></th>
        <th><a href="../arxiv/magnon">Magnon</a></th>
        <th><a href="../arxiv/majorana">Majorana</a></th>
    </tr>
    <tr>
       <th><a href="../arxiv/metric">Metric</a></th>
       <th><a href="../arxiv/nematic">Nematic</a></th>
       <th><a href="../arxiv/nickelate">Nickelate</a></th>
      <th><a href="../arxiv/shiftcurrent">Shift current</a></th>
       <th><a href="../arxiv/skyrmion">Skyrmion</a></th>
       <th></th>
    </tr>
    <tr>
       <th><a href="../arxiv/spin">Spin</a></th>
       <th><a href="../arxiv/strain">Strain</a></th>
       <th><a href="../arxiv/theory">Theory</a></th>
       <th><a href="../arxiv/wave">Wave</a></th>
       <th></th>
       <th></th>
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
  <br>
  <a href="#" onclick="window.open('https://claude.ai', '_blank', 'width=1000,height=600');"> claude.ai </a>
  <br>
  <a href="#" onclick="window.open('https://chatgpt.com', '_blank', 'width=1000,height=600');"> chatgpt.com </a>
  <br>
   
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
