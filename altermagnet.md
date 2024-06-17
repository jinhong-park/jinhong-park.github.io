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
        <li class="listing-item" id="post-{{ forloop.index }}">
            {{ post.content }}
        </li>
    {% endfor %}
</ul>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var keyword = "alter";
        var posts = document.querySelectorAll(".listing-item");
        posts.forEach(function(post) {
            var lines = post.innerHTML.split('\n');
            var matchingLines = lines.filter(function(line) {
                return line.includes(keyword);
            });
            post.innerHTML = matchingLines.join('<br>');
        });
    });
</script>