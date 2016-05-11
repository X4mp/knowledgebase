---
layout: page
title: Tags
hidden: true
---

<span class="discreet"><a href="/posts">Sort by date</a></span>

{% assign sorted_tags = (site.tags | sort:0) %}
{% for tag in sorted_tags  %}
  <h3 id="{{ tag[0] }}-ref">{{ tag[0] }}</h3>
  <ul>
    {% assign post_list = tag[1] %}
    {% for post in post_list %}
         <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
