---
title: Archive
layout: page
permalink: archive/
description: View compiled results for any year.
intro_image_absolute: true
intro_image_hide_on_mobile: false
---

<div class="col-12">
{% for post in site.posts %}
  <div class="service service-summary">
    <div class="service-content">
      <h2 class="service-title">
      <a href="{{ site.baseurl}}{{ post.url }}">{{ post.title }}</a>
     </h2>
   <p>{{ result.content | markdownify | strip_html | truncate: 100 }}</p>
  </div>
</div>
{% endfor %}
</div>
