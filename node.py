from select import select
import rospy


class Node:
    def __init__(self, name: str):
        rospy.init_node(name)
        self.name = name
        self.publishers = dict()
        self.subscribers = dict()

    def init_publisher(
        self, name: str, publish_to: str, MessageType, queue_size=1, **kwargs
    ):
        self.publishers[name] = rospy.Publisher(
            publish_to, MessageType, queue_size=queue_size, **kwargs
        )

    def publish(self, name, msg):
        self.publishers[name].publish(msg)

    def init_subscriber(
        self, name: str, subscibe_to: str, MessageType, callback, queue_size=1, **kwargs
    ):
        self.subscribers[name] = rospy.Subscriber(
            "subscibe_to",
            MessageType,
            callback=callback,
            queue_size=queue_size,
            **kwargs
        )

    def spin(self):
        rospy.spin()
