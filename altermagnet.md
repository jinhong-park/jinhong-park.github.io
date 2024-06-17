---
layout: page
title: altermagnet
permalink: /altermagnet
---
 
<a href="https://jinhong-park.github.io/t_me">Daily t.me</a>
<br>
<a href="#" onclick="window.open('https://ui.adsabs.harvard.edu', '_blank', 'width=1000,height=600');">Good Luck Search using Adsabs</a>
<br>
<a href="#" onclick="window.open('https://scholar.google.com', '_blank', 'width=1000,height=600');">Google Scholar</a>
<br>
<a href="#" onclick="window.open('https://typeset.io', '_blank', 'width=1000,height=600');">Typeset.io</a>

<ul class="listing">
    {% assign keyword = "alter" %}
    {% for post in site.posts %}
        <li class="listing-seperator">
            <p>{{ post.title }}</p>
        </li>
        <li class="listing-item">
            {% assign lines = post.content | split: '\n' %}
            {% for line in lines %}
                {% if line contains keyword %}
                    <p>{{ line }}</p>
                {% endif %}
            {% endfor %}
        </li>
    {% endfor %}
</ul>