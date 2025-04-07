#!/usr/bin/env python3
"""
AI Secretary Architecture Diagram Generator
-------------------------------------------
This script generates a visualization of the AI Secretary mobile app architecture.
The diagram shows the relationships between different components and layers.
"""

import graphviz
import os

# Create a new directed graph
dot = graphviz.Digraph('AI_Secretary_Architecture', comment='AI Secretary Architecture')

# Set graph attributes
dot.attr(rankdir='TB', size='8,10', dpi='300', fontname='Arial',
         bgcolor='white', nodesep='0.5', ranksep='1')

# Cluster for Frontend (Flutter)
with dot.subgraph(name='cluster_frontend') as c:
    c.attr(label='Frontend Layer (Flutter)', style='filled', color='#E0F2F1', fontsize='18')

    c.node('ui_components', 'UI Components\n(Dashboard, Inbox, Calendar, Voice)',
           shape='box', style='filled', fillcolor='#4DB6AC')
    c.node('state_mgmt', 'State Management\n(Provider Pattern)',
           shape='box', style='filled', fillcolor='#4DB6AC')
    c.node('cross_platform', 'Cross-Platform Support\n(Material Design 3)',
           shape='box', style='filled', fillcolor='#4DB6AC')

    c.edge('ui_components', 'state_mgmt')
    c.edge('state_mgmt', 'cross_platform')

# Cluster for Orchestration (LangGraph)
with dot.subgraph(name='cluster_langgraph') as c:
    c.attr(label='Orchestration Layer (LangGraph)', style='filled', color='#FFF3E0', fontsize='18')

    c.node('state_graph', 'State Management\n(StateGraph)',
           shape='box', style='filled', fillcolor='#FFB74D')
    c.node('cognitive_flows', 'Cognitive Flows\n(Task, Calendar, Email, Voice)',
           shape='box', style='filled', fillcolor='#FFB74D')
    c.node('tool_integration', 'Tool Integration',
           shape='box', style='filled', fillcolor='#FFB74D')
    c.node('hitl', 'Human-in-the-Loop\nCapabilities',
           shape='box', style='filled', fillcolor='#FFB74D')

    c.edge('state_graph', 'cognitive_flows')
    c.edge('cognitive_flows', 'tool_integration')
    c.edge('tool_integration', 'hitl')

# Cluster for Backend Services
with dot.subgraph(name='cluster_backend') as c:
    c.attr(label='Backend Services', style='filled', color='#E8EAF6', fontsize='18')

    c.node('auth_service', 'Authentication\nService',
           shape='box', style='filled', fillcolor='#7986CB')
    c.node('ai_service', 'AI Model\nService',
           shape='box', style='filled', fillcolor='#7986CB')
    c.node('sync_service', 'Sync\nService',
           shape='box', style='filled', fillcolor='#7986CB')
    c.node('integration_service', 'Integration\nServices',
           shape='box', style='filled', fillcolor='#7986CB')

# Cluster for On-Device Inference
with dot.subgraph(name='cluster_inference') as c:
    c.attr(label='On-Device Inference', style='filled', color='#FFEBEE', fontsize='18')

    c.node('whisper', 'Whisper.cpp\n(Speech-to-Text)',
           shape='box', style='filled', fillcolor='#EF9A9A')
    c.node('llama', 'llama.cpp\n(Lightweight LLM)',
           shape='box', style='filled', fillcolor='#EF9A9A')
    c.node('mlc_llm', 'MLC LLM\n(Mobile Inference)',
           shape='box', style='filled', fillcolor='#EF9A9A')
    c.node('local_vector', 'Local Vector DB\n(SQLite-based)',
           shape='box', style='filled', fillcolor='#EF9A9A')

# Cluster for Data Persistence
with dot.subgraph(name='cluster_data') as c:
    c.attr(label='Data Persistence', style='filled', color='#E0F7FA', fontsize='18')

    c.node('local_storage', 'Local Storage\n(SQLite, Vectors, Files)',
           shape='box', style='filled', fillcolor='#4DD0E1')
    c.node('cloud_storage', 'Cloud Storage\n(Optional)',
           shape='box', style='filled', fillcolor='#4DD0E1')
    c.node('memory_mgmt', 'Memory Management\n(Conversation History)',
           shape='box', style='filled', fillcolor='#4DD0E1')

# Cloud & Device
dot.node('mobile_device', 'Mobile Device', shape='box3d', style='filled', fillcolor='#E8F5E9')
dot.node('cloud', 'Cloud Services', shape='cloud', style='filled', fillcolor='#B3E5FC')

# Add connecting edges between clusters
dot.edge('state_mgmt', 'state_graph')
dot.edge('cognitive_flows', 'auth_service')
dot.edge('tool_integration', 'integration_service')
dot.edge('ai_service', 'cloud')
dot.edge('sync_service', 'cloud')
dot.edge('state_graph', 'local_storage')
dot.edge('whisper', 'cognitive_flows')
dot.edge('llama', 'cognitive_flows')
dot.edge('mlc_llm', 'cognitive_flows')
dot.edge('local_vector', 'local_storage')
dot.edge('ui_components', 'mobile_device')
dot.edge('mobile_device', 'whisper')
dot.edge('mobile_device', 'llama')
dot.edge('cloud', 'sync_service')
dot.edge('local_storage', 'mobile_device')
dot.edge('cloud_storage', 'cloud')
dot.edge('memory_mgmt', 'state_graph')

# Add a hybrid processing flow
dot.edge('mobile_device', 'cloud', color='blue', style='dashed', label='Hybrid Processing')

# Render the diagram
dot.render('ai_secretary_architecture', format='png', cleanup=True)
print(f"Architecture diagram created: ai_secretary_architecture.png")

# If you want to generate SVG as well
dot.render('ai_secretary_architecture', format='svg', cleanup=True)
print(f"SVG diagram also created: ai_secretary_architecture.svg")