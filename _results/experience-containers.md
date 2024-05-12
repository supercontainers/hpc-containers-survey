---
title: "How do you rate your experience with containers?"
date: 2024-05-12T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# How do you rate your experience with containers?

## 2024

{% assign counts = site.data.cleaned.containers-in-hpc-2024["How do you rate your experience with containers?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2024" %}
