# StatefulSet:

**serviceName**: The name of the headless service used to manage network identities for the StatefulSet.

**replicas**: Number of replicas for the StatefulSet.

**selector**: Selects pods with the label app: mysql.

**template**: Contains the pod template for the StatefulSet.

**containers**: Specifies the container image (MySQL in this case), port, environment variables, and volume mounts.

**volumeMounts**: Mounts the PVC to the container.

**volumeClaimTemplates**: Defines a PVC template to provision storage for the MySQL database.

# Service:

**clusterIP**: None: Configures the service as headless to enable StatefulSet network identity.