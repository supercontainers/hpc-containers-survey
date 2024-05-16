---
title: "The HPC Container Community Survey"
date: 2024-05-16
draft: false
layout: post
---

This is the first HPC Container Community Survey that will provide insights to container usage of the HPC community. The idea was originally proposed as part of the <a href="https://supercontainers.github.io/containers-wg/ideas/container-technologies-survey/" target="_blank">Containers Working Group</a>, but it was stopped in its tracks. Earlier this year we realized how valuable the insights would be, even to understand basics about container technology usage, and the effort was rekindled. We got <span style="font-weight:600">202 responses</span> in total, presenting the results at the <a href="https://www.linkedin.com/posts/isc-hpc_isc24-reinventinghpc-hpc-activity-7196781879134429187-PmFf?utm_source=share&utm_medium=member_desktop" target="_blank">High Performance Container Workshop</a> (<a href="https://container-in-hpc.org/isc/2024/hpcw/index.html" target="_blank">agenda</a>). We think that this first year was great success!

<iframe width="100%" height="400" src="https://www.youtube.com/embed/RgMDAT7lHU4?si=_KkeyON1xFWN_Km0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<div class="call-box-bottom" style="padding-bottom:50px">
  <a href="{{ site.baseurl }}/results/" class="button">View Full Results</a>
</div>

<br>

# About People

## What is your primary role

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What is your primary role?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_role_2024" %}

The leading category is System Administrator, followed by Research Software Engineer, Software Engineer, and then Manager
and Computer Scientist. We believe this sample explains why most of survey respondents reported having intermediate or
expert level experience with containers - these are the folks actively provisioning, building, and supporting the container
technologies. In future years we might consider expanding the audience out to more scientific communities to get feedback
from more beginners.

<p class="team team-summary team-summary-large">We can tell from this question that we have a diverse community.</p>

## What is your primary environment

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What is your primary environment?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_environment_2024" %}

Most of you are in academia, followed by commercial environments and national laboratories and even consulting. This
is both an expected result and fantastic to see the diversity of our community.

<p class="team team-summary team-summary-large">Container usage in HPC spans academia, national labs, industry, and beyond.</p>

## How do you rate your experience with containers?


{% assign counts = site.data.cleaned.containers-in-hpc-2024["How do you rate your experience with containers?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_experience_2024" %}

It was surprising to see the majority of respondents report intermediate to expert usage. We likely need to do a better job to engage with beginner container users.

<p class="team team-summary team-summary-large">The majority of the HPC containers community that we surveyed reports intermediate to expert ability.</p>


## Do you develop container technologies or related tooling?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you develop container technologies or related tooling?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_developers_2024" %}

The HPC containers community has a lot of developers! This question would be interesting to expand out into the kind of developer. For
example, a core container technology is different from a container orchestration tool, which is also different than a metadata extraction tool.

<p class="team team-summary team-summary-large">Developers, developers, developers! We have a surprisingly large developer base in this survey audience.</p>

<br>

# About Container Technologies

## Which container technologies are supported on the system(s) you are working on?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Which container technologies are supported on the system(s) you are working on?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_tech_supported_2024" %}

Singularity / Apptainer is the most commonly provided container technology, followed by Docker and Podman. It's not clear in what context Docker is being provided.
We likely need to expand the questions to ask about the type of cluster or resource where the container technology is provided to give better insight to this answer.

<p class="team team-summary team-summary-large">It's clear that centers provide a range of supported technologies, with a handful being more likely to be found than others.</p>

## On those same systems and out of the set above, which HPC container technologies are you using?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["On those same systems and out of the set above, which HPC container technologies are you using?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_tech_used_2024" %}

The usage mirrors the provision, albeit fewer people report using each. For Singularity, the difference is small (~20), but for Docker (~35) and Podman (of those that reported their center provided it, only half actually report using it) the differences are larger. This question suggests that centers should keep abreast of what users want to use vs. what is provided.

<p class="team team-summary team-summary-large">However, of that set, a fewer number are reported to be used regularly.</p>


## What container technologies do you use on your local machine(s), personal or for work?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What container technologies do you use on your local machine(s), personal or for work?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_local_machine_2024" %}

Logically, Docker (and having root) is a standard and the preferred container technology when we have full control. Of the rootless "HPC" set, Singularity / Apptainer is next, followed by Podman.

<p class="team team-summary team-summary-large">For local usage, Docker is king.</p>


## Which HPC container technologies have you not used that you would like to use?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Which HPC container technologies have you not used that you would like to use?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_like_to_use_2024" %}

This question is interesting because the majority of people aren't interested in trying a new one, suggesting they are satiated, or at least not interested in other options they have not tried.
It's not clear if people chose responses for the other technologies just for the heck of it (and don't intend to actually try them) or if these individuals will make a concerted effort to try them.
My (@vsoch) guess is the first - it's a survey question that people were providing an answer to, and they likely won't prioritize going out of their way to try a new one. What additional information is needed here is to ask why they want to try a new one. Likely a missing feature or ability is a stronger driver than "Sure, might be fun."

<br>

# About Images

## What specification or recipe do you use to build containers?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What specification or recipe do you use to build containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_recipe_2024" %}

Dockerfile is the clear leader here, and this makes sense because the other container technologies have support for either interacting with it directly, or pulling down containers built from it.

## Do you use any supporting tools to build containers?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you use any supporting tools to build containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_supporting_tooling_2024" %}

Our HPC package managers are leaders in helping us to build containers.

## Once built, do you tend to push containers to a central registry?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Once built, do you tend to push containers to a central registry?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_push_registry_2024" %}

The fact that almost half of the community is not pushing images to a central registry is concerning, as it indicates reproducibility might be less likely. If you need help with creating a CI/CD pipeline or exploring options for registries (public or private) you can ask your local HPC administrator or research software engineers.
This could also reflect the survey population in that the majority of HPC administrators provide container technologies but do not actively build them.

## What container registries are you pushing builds to?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["What container registries are you pushing builds to?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_registries_2024" %}

We have a lot of registries, and despite a few issues over the years, Docker Hub is still the leader. GitLab is a close second, which might be a reflection of the fact it can be self-hosted and thus provided by national labs and academic centers on premises. GitHub packages and Quay.io are next in line, and GitHub packages makes sense as it is tightly paired with GitHub actions, the CI/CD service for GitHub.

## In what context(s) are you using containers?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["In what context(s) are you using containers?"].counts %}
{% include graphs/bar.html counts=counts divid="chart_contexts_2024" %}

Using containers for HPC applications and simulations makes sense, as does for developer environments (on local machines or remote) and Kubernetes. The surprising result here was the case of provisioning use.

<br>

# Finishing Up


## Do you typically have to build containers for multiple architectures?


{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you typically have to build containers for multiple architectures?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_arch_2024" %}

The majority of our community is building for one architecture, but there is a non-insignificant number that are building for others, so it is a valid use case that deserves attention.

## Do you use CI/CD for automated build and deploy?

{% assign counts = site.data.cleaned.containers-in-hpc-2024["Do you use CI/CD for automated build and deploy?"].counts %}
{% include graphs/pie.html counts=counts divid="chart_cicd_2024" %}

This result could be reflective of the survey population, and that the majority of, for example, HPC administrators aren't actively building and testing containers. If it's reflective of overall practives, the result is more concerning. If almost half of you aren't using CI/CD for automated deploy, please consult a research software engineer or support staff if you'd like to do this but do not know how.

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
