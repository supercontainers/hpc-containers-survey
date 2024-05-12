---
title: "How often do you use containers?"
date: 2024-05-12T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# How often do you use containers?

## 2024

{% assign counts = site.data.cleaned.containers-in-hpc-2024["How often do you use containers?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_usage_2024" %}
