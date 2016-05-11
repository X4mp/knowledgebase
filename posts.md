---
layout: page
title: Posts
permalink: /posts/
---

<span class="discreet"><a href="/tags">Sort by tag</a></span>

{% for post in site.posts %}
   {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
   {% capture next_year %}{{ post.next.date | date: "%Y" }}{% endcapture %}

   {% if forloop.first %}
<h3>{{this_year}}</h3>
<ul>
    {% else %}
        {% if this_year != next_year %}
</ul>
<h3>{{this_year}}</h3>
<ul>
        {% endif %}
    {% endif %}
   <li><!--{{ post.date | date: "%b %-d, %Y" }} --> <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></li>

   {% if forloop.last %}
</ul>
   {% endif %}
{% endfor %}


subscribe [via Atom]({{ "/feed.xml" | prepend: site.baseurl }})
