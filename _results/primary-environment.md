---
title: "Primary Environment"
date: 2024-05-12T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# What is your primary environment

## 2024

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What is your primary environment?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_2024" %}
