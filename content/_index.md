---
title: ACP Lab
type: landing

sections:
  # Full-screen looping lab footage. To refresh: replace static/media/hero.mp4 and
  # static/media/hero-poster.jpg (H.264 MP4, muted, keep under ~8 MB).
  - block: video-hero
    id: hero
    content:
      video: media/hero.mp4
      poster: media/hero-poster.jpg
      headline: Agile aerial robots that carry, manipulate, and collaborate
      subline: We are the Aerial-robot Control and Perception (ACP) Lab at Worcester Polytechnic Institute. We develop the planning, control, and perception that let flying robots interact physically with the world — and with people.
      buttons:
        - text: Explore Our Research
          url: research/
          primary: true
        - text: Join the Lab
          url: join/

  # Compact teaser of the three research pillars (full venn diagram lives on the Research page).
  # Keep these entries in sync with content/research/_index.md.
  - block: pillars
    id: research
    content:
      title: Three Research Pillars
      subtitle: Click a pillar to explore the related publications.
      pillars:
        - title: Aerial Robot Agility, Intelligence and Safety
          description: Fast, dynamics-aware planning and control, robust perception and estimation, learning-based models, and safety guarantees that let single aerial robots fly aggressively and reliably.
          url: research/agility-intelligence-safety/
          icon: eagle-agile-b
          icon_pack: custom
          tint: '#9cc0ff'
          tint_light: '#dbe7ff'
          accent: '#2563eb'
        - title: Aerial Physical Intelligence
          description: Aerial robots that carry, manipulate, and make contact with the world, from cable-suspended payloads and perching to tactile control and physical collaboration with people.
          url: research/aerial-physical-intelligence/
          icon: eagle-arm
          icon_pack: custom
          tint: '#7fe3d2'
          tint_light: '#d2f7f0'
          accent: '#0f9d8a'
        - title: Multi-Robot Collaboration
          description: Teams of aerial robots that cooperatively transport and manipulate objects, self-assemble into modular structures, avoid each other safely, and collaborate with humans.
          url: research/multi-robot-collaboration/
          icon: eagle-trio
          icon_pack: custom
          tint: '#c7b6ff'
          tint_light: '#e9e2ff'
          accent: '#7c3aed'
    design:
      columns: '1'
      show_venn: false

  - block: collection
    id: news
    content:
      title: Recent News
      text:
      count: 3
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: compact
      columns: '1'

  - block: collection
    id: featured
    content:
      title: Featured Publications
      filters:
        folders:
          - journal
          - conference
        featured_only: false
      text:
      count: 5
    sort_by: 'Date'
    design:
      columns: '1'
      view: custom

  - block: sponsors
    id: sponsors
    content:
      title: Our Sponsors
      subtitle: We gratefully acknowledge the support of our sponsors.
      sponsors:
        - name: National Science Foundation
          image: logos/nsf.png
          url: https://www.nsf.gov/
        - name: Amazon Robotics
          image: logos/amazon-robotics.png
          url: https://www.amazon.science/research-areas/robotics
    design:
      columns: '1'
      logo_height: 96px
---
