---
title: Student Projects
type: landing

sections:
  - block: portfolio
    id: projects
    content:
      title: Student Projects
      subtitle: Open projects for WPI students. Filter by topic and click a card to read the details and desired skills.
      filters:
        folders:
          - projects
      # Default filter index (0 = All)
      default_button_index: 0
      buttons:
        - name: All
          tag: '*'
        - name: Control
          tag: control
        - name: Learning
          tag: learning
        - name: Perception
          tag: perception
        - name: Safety
          tag: safety
        - name: Multi-Robot
          tag: multi-robot
        - name: Human-Robot Interaction
          tag: human-robot interaction
        - name: Software
          tag: software
    design:
      columns: '1'
      view: masonry
      flip_alt_rows: false
---
