---
title: "Once built, do you tend to push containers to a central registry?"
date: 2024-05-12T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# Once built, do you tend to push containers to a central registry?

## 2024

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Once built, do you tend to push containers to a central registry?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2024" %}
