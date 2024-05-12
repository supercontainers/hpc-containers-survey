---
title: "What container registries are you pushing builds to?"
date: 2024-05-12T12:33:46+10:00
featured: true
weight: 1
layout: result
---

# What container registries are you pushing builds to?

## 2024

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What container registries are you pushing builds to?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_2024" %}

