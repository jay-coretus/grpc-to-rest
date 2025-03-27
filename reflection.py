import grpc
from google.protobuf import descriptor_pb2
from google.protobuf.descriptor_pool import DescriptorPool
from leobrain_protos_new.user_service import user_pb2

# Mapping of protobuf field types to human-readable strings
FIELD_TYPES = {
    descriptor_pb2.FieldDescriptorProto.TYPE_DOUBLE: "double",
    descriptor_pb2.FieldDescriptorProto.TYPE_FLOAT: "float",
    descriptor_pb2.FieldDescriptorProto.TYPE_INT64: "int64",
    descriptor_pb2.FieldDescriptorProto.TYPE_UINT64: "uint64",
    descriptor_pb2.FieldDescriptorProto.TYPE_INT32: "int32",
    descriptor_pb2.FieldDescriptorProto.TYPE_FIXED64: "fixed64",
    descriptor_pb2.FieldDescriptorProto.TYPE_FIXED32: "fixed32",
    descriptor_pb2.FieldDescriptorProto.TYPE_BOOL: "bool",
    descriptor_pb2.FieldDescriptorProto.TYPE_STRING: "string",
    descriptor_pb2.FieldDescriptorProto.TYPE_GROUP: "group",
    descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE: "message",
    descriptor_pb2.FieldDescriptorProto.TYPE_BYTES: "bytes",
    descriptor_pb2.FieldDescriptorProto.TYPE_UINT32: "uint32",
    descriptor_pb2.FieldDescriptorProto.TYPE_ENUM: "enum",
    descriptor_pb2.FieldDescriptorProto.TYPE_SFIXED32: "sfixed32",
    descriptor_pb2.FieldDescriptorProto.TYPE_SFIXED64: "sfixed64",
    descriptor_pb2.FieldDescriptorProto.TYPE_SINT32: "sint32",
    descriptor_pb2.FieldDescriptorProto.TYPE_SINT64: "sint64"
}

# Mapping of label types to human-readable strings
LABEL_TYPES = {
    descriptor_pb2.FieldDescriptorProto.LABEL_OPTIONAL: "optional",
    descriptor_pb2.FieldDescriptorProto.LABEL_REQUIRED: "required",
    descriptor_pb2.FieldDescriptorProto.LABEL_REPEATED: "repeated"
}

def get_service_methods(service_descriptor):
    """
    Extract methods and their input/output message definitions for a given service.
    
    Args:
        service_descriptor: The service descriptor from the protobuf file
    
    Returns:
        A list of dictionaries containing method details
    """
    methods_info = []
    
    for method in service_descriptor.methods:
        method_info = {
            "name": method.name,
            "input_type": method.input_type.name,
            "output_type": method.output_type.name
        }
        methods_info.append(method_info)
    
    return methods_info

def get_message_definition(descriptor_pool, message_descriptor):
    """
    Retrieve the full message definition for a given message descriptor.
    
    Args:
        descriptor_pool: The descriptor pool containing protobuf definitions
        message_descriptor: Descriptor of the message to retrieve
    
    Returns:
        A dictionary of field definitions for the message
    """
    try:
        fields = []
        
        for field in message_descriptor.fields:
            field_info = {
                "name": field.name,
                "number": field.number,
                "type": FIELD_TYPES.get(field.type, f"unknown_type_{field.type}"),
                "label": LABEL_TYPES.get(field.label, f"unknown_label_{field.label}")
            }
            fields.append(field_info)
        
        return {
            "name": message_descriptor.name,
            "fields": fields
        }
    except Exception as e:
        return {"name": message_descriptor.name, "error": str(e)}

def main():
    # Get the descriptor pool from the generated protobuf module
    descriptor_pool = user_pb2.DESCRIPTOR.pool
    
    # Find the UserService in the descriptor pool
    service_descriptor = descriptor_pool.FindServiceByName("userservice.UserService")
    
    # Get all methods for the service
    methods = get_service_methods(service_descriptor)
    
    # Collect detailed information about methods and their messages
    detailed_methods = []
    
    for method in methods:
        method_details = method.copy()
        
        # Get input message descriptor
        input_message_descriptor = descriptor_pool.FindMessageTypeByName(f"userservice.{method['input_type']}")
        
        # Get output message descriptor
        output_message_descriptor = descriptor_pool.FindMessageTypeByName(f"userservice.{method['output_type']}")
        
        # Get input and output message definitions
        input_message = get_message_definition(descriptor_pool, input_message_descriptor)
        output_message = get_message_definition(descriptor_pool, output_message_descriptor)
        
        method_details['input_message'] = input_message
        method_details['output_message'] = output_message
        
        detailed_methods.append(method_details)
    
    # Pretty print the results
    import json
    print(json.dumps(detailed_methods, indent=2))

if __name__ == "__main__":
    main()