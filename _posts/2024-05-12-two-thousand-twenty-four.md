---
title: "The HPC Container Community Survey"
date: 2024-05-12
draft: false
layout: post
---

The HPC Container Community Survey has been a long time coming. We kicked off the idea as part of the [Containers Working Group](https://supercontainers.github.io/containers-wg/ideas/container-technologies-survey/) but it stopped in its tracks due to too many cooks in the kitchen, and "perfection is the enemy of the good." Earlier this year we realized how valuable the insights would be, even to understand basics about container technology usage, and the effort was rekindled.

<div class="call-box-bottom" style="padding-bottom:50px">
  <a href="{{ site.baseurl }}/results/" class="button">View Full Results</a>
</div>


<br>

# About People

## What is your primary role

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What is your primary role?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_role_2024" %}

<p class="team team-summary team-summary-large">We can tell from this question that we have a diverse community.</p>

## What is your primary environment

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What is your primary environment?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_environment_2024" %}

<p class="team team-summary team-summary-large">Container usage in HPC spans academia, national labs, industry, and beyond.</p>

## How do you rate your experience with containers?


{% assign counts = site.data.cleaned.containers-in-hpc-2024["How do you rate your experience with containers?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_experience_2024" %}

<p class="team team-summary team-summary-large">It was surprising to see the majority of respondents report intermediate to expert usage. We likely need to do a better job to engage with beginner container users.</p>


## Do you develop container technologies or related tooling?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you develop container technologies or related tooling?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_developers_2024" %}

<p class="team team-summary team-summary-large">Developers, developers, developers! We have a surprisingly large developer base in this survey audience.</p>


<br>

# About Container Technologies

## Which container technologies are supported on the system(s) you are working on?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Which container technologies are supported on the system(s) you are working on?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_tech_supported_2024" %}

<p class="team team-summary team-summary-large">It's clear that centers provide a range of supported technologies, with a handful being more likely to be found than others.</p>

## On those same systems and out of the set above, which HPC container technologies are you using?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["On those same systems and out of the set above, which HPC container technologies are you using?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_tech_used_2024" %}

<p class="team team-summary team-summary-large">However, of that set, a fewer number are reported to be used regularly.</p>


## What container technologies do you use on your local machine(s), personal or for work?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What container technologies do you use on your local machine(s), personal or for work?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_local_machine_2024" %}

<p class="team team-summary team-summary-large">For local usage, Docker is king.</p>


## Which HPC container technologies have you not used that you would like to use?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Which HPC container technologies have you not used that you would like to use?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_like_to_use_2024" %}

<br>

# About Images

## What specification or recipe do you use to build containers?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What specification or recipe do you use to build containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_recipe_2024" %}

## Do you use any supporting tools to build containers?


{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you use any supporting tools to build containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_supporting_tooling_2024" %}


## Once built, do you tend to push containers to a central registry?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Once built, do you tend to push containers to a central registry?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_push_registry_2024" %}

## What container registries are you pushing builds to?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What container registries are you pushing builds to?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_registries_2024" %}

## In what context(s) are you using containers?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["In what context(s) are you using containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_contexts_2024" %}


<br>

# Finishing Up


## Do you typically have to build containers for multiple architectures?


{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you typically have to build containers for multiple architectures?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_arch_2024" %}

## Do you use CI/CD for automated build and deploy?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you use CI/CD for automated build and deploy?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_cicd_2024" %}


## What are you biggest challenges or pain points when using containers, or reasons that you don't use them?

{% assign values = site.data.cleaned.containers-in-hpc-2024["What are you biggest challenges or pain points when using containers, or reasons that you don't use them?"].values %}
{% include graphs/cloud.html values=values divid="cloud_challenges_2024" %}

{% assign values = site.data.cleaned.containers-in-hpc-2024["What are you biggest challenges or pain points when using containers, or reasons that you don't use them?"].values %}
{% include summary/listing.html values=values divid="values_challenges_2024" %}

# What can containers not do that you wish they could? What features would you like to see?

{% assign values = site.data.cleaned.containers-in-hpc-2024["What can containers not do that you wish they could? What features would you like to see?"].values %}
{% include graphs/cloud.html values=values divid="cloud_features_2024" %}

{% assign values = site.data.cleaned.containers-in-hpc-2024["What can containers not do that you wish they could? What features would you like to see?"].values %}
{% include summary/listing.html values=values divid="values_features_2024" %}
