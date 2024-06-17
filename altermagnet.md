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

<ul class="listing" id="posts-listing">
    {% for post in site.posts %}
        <li class="listing-seperator" id="title-{{ forloop.index }}" style="display: none;">
            <p>{{ post.title }}</p>
        </li>
        <li class="listing-item" id="post-{{ forloop.index }}" style="display: none;">
            {{ post.content | escape }}
        </li>
    {% endfor %}
</ul>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var keyword = "alter";
        var excludeKeywords = ["alternative", "alternating"];
        var posts = document.querySelectorAll(".listing-item");
        posts.forEach(function(post, index) {
            var lines = post.textContent.split('\n');
            var includePost = false;
            lines.forEach(function(line) {
                if (line.includes(keyword)) {
                    var excludeFound = excludeKeywords.some(function(excludeKeyword) {
                        return line.includes(excludeKeyword);
                    });
                    if (!excludeFound) {
                        includePost = true;
                    }
                }
            });
            if (includePost) {
                post.innerHTML = lines.join('<br>');
                post.style.display = "block";
                var title = document.getElementById('title-' + (index + 1));
                if (title) {
                    title.style.display = "block";
                }
            }
        });
    });
</script>