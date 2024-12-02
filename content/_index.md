---
title: ACP Lab 
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: 👋 Welcome to the ACP Lab
          content: Take a look at what we're working on...
          align: center
          background:
            image:
              # Specify an image from `assets/media/`
              # or delete the image section to remove it
              filename: 
              filters:
                brightness: 0.7
            position: right
            color: '#666'
        - title: HPA-MPC has been accepted to RA-L!
          content:  
          align: center
          background:
            image:
              filename: albums/test/human_robot_interaction_2.jpg
              filters:
                brightness: 0.7
            position: right
            color: '#666'        
        - title: Human-Aware Physical Human-Robot Collaborative Transportation and Manipulation with Multiple Aerial Robots Has Been Accepted by T-RO!
          content: 
          align: left
          background:
            image:
              filename: albums/test/human-multi-robot-interaction.jpg
              filters:
                brightness: 0.7
            position: center
            color: '#555'
        - title: ACP Lab
          content: 'Just opened!'
          align: right
          background:
            image:
              filename:  
              filters:
                brightness: 0.5
            position: center
            color: '#333'
          link:
            icon: graduation-cap
            icon_pack: fas
            text: Join Us
            url: ../contact/ 
        - title: Welcome to Cyberbotics Lab
          content: Our research focuses on __Cyber__-Physical and Ro**botics** (Cyberbotics) systems, with a primary emphasis on bipedal walking robots.
          align: center
          background:
            image:
              filename: 
              filters:
                brightness: 0.4
            position: center 
            color: '#333'
          link:
            icon: book-open-reader #graduation-cap
            icon_pack: fas
            text: Explore Our Research
            url: ../projects/
        - title: __Meet Our Team__
          content: A diverse and talented group of researchers dedicated to scientific excellence.
          align: left
          background:
            image:
              filename: 
              filters:
                brightness: 0.4
            position: center
            color: '#555'
          link:
            icon: graduation-cap
            icon_pack: fas
            text: Meet Our Team
            url: ../people/
          # link:
          #   icon: graduation-cap
          #   icon_pack: fas
          #   text: Join Us
          #   url: ../contact/
        - title: Meet Our Robots
          content: 'Uniquely equipped to support groundbreaking discoveries.'
          align: right
          background:
            image:
              filename: 
              filters:
                brightness: 0.4
            position: center
            color: '#555'
          link:
            icon: robot
            icon_pack: fas
            text: Robot Videos
            url: ../videos/    
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: true
      # Duration of transition between slides (in ms)
      interval: 5000     

  - block: collection
    content:
      title: Recent News
      # subtitle: |-
        # {{% callout hint %}}
        # See all [news](./post/).
        # {{% /callout %}}
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
      columns: 1'

  - block: collection
    id: projects
    content:
      title: Research Projects
      subtitle: |-
        {{% callout hint %}}
        See all [projects](./projects/).
        {{% /callout %}}
      filters:
        folders:
          - project
        featured_only: false
      text: 
      count: 3
    design:
      columns: '1'
      view: showcase
      flip_alt_rows: false
     
  - block: collection
    id: featured
    content:
      title: Featured Publications
      # subtitle: |-
      #   {{% callout hint %}}
      #   See all [publications](./publication/).
      #   {{% /callout %}}
      filters:
        folders:
          - publication
        featured_only: true
      text: 
      count: 5
    design:
      columns: '1'
      view: custom
  

  # - block: logos
  #   content:
  #     title: Section Title
  #     subtitle: Section Subtitle
  #     # Path to the logo images within the `assets/media/` folder
  #     logo_folder: logos
  #   design:
  #     columns: '1'  

  - block: tag_cloud
    content:
      title: Popular Topics
      # subtitle: My subtitle
      # text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 20
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 1.0
      font_size_max: 2
      columns: '1'
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: 2
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle:
  #     text: |
  #       {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
  #   design:
  #     columns: '2'
---