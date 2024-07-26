Components

# ConfigMap

Purpose: Stores the Fluent Bit configuration file, which defines how logs are collected and where they are sent.
Usage: Used by the Fluent Bit DaemonSet to configure the log collection and forwarding behavior.

# DaemonSet

Purpose: Ensures that a Fluent Bit pod runs on every node in the Kubernetes cluster.
Usage: Automatically deploys Fluent Bit on all nodes to collect logs from all containers.

# RBAC 

Purpose: Provides necessary permissions if Kubernetes Role-Based Access Control (RBAC) is enabled.
Usage: Defines roles and bindings that grant Fluent Bit access to Kubernetes API resources needed for log collection.

# ServiceAccount

Purpose: Uses a dedicated ServiceAccount for Fluent Bit, which can be helpful for managing permissions and access control.
Usage: Assigns a specific identity to the Fluent Bit pods, which is especially useful if you need custom RBAC policies.

# Summary of Setup

Apply ConfigMap:

Loads the Fluent Bit configuration into Kubernetes so that Fluent Bit can use it to collect and forward logs.
Apply DaemonSet:

Deploys Fluent Bit on each node to ensure logs from all containers are collected.
Apply RBAC:

Sets up roles and permissions if your cluster uses RBAC, ensuring Fluent Bit can access necessary resources.
Apply ServiceAccount:

Creates a dedicated ServiceAccount for Fluent Bit, useful for managing permissions and improving security.
Validation
DaemonSet Check: Verify that Fluent Bit pods are running on all nodes.
Log Check: Inspect Fluent Bit logs to ensure it's collecting and forwarding logs as expected.