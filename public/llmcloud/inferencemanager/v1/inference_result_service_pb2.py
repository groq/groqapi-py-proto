# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public/llmcloud/inferencemanager/v1/inference_result_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBpublic/llmcloud/inferencemanager/v1/inference_result_service.proto\x12#public.llmcloud.inferencemanager.v1\x1a\x1egoogle/protobuf/duration.proto\")\n\'InferenceResultServiceGetResultResponse\"z\n\x0fProcessingStats\x12)\n\x10tokens_processed\x18\x01 \x01(\rR\x0ftokensProcessed\x12<\n\x0cprocess_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bprocessTime\"|\n\x0fGenerationStats\x12)\n\x10tokens_generated\x18\x01 \x01(\rR\x0ftokensGenerated\x12>\n\rgenerate_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0cgenerateTime\"\x96\x03\n&InferenceResultServiceGetResultRequest\x12\x14\n\x05token\x18\x01 \x01(\rR\x05token\x12\x1d\n\nrequest_id\x18\x02 \x01(\tR\trequestId\x12)\n\x10response_address\x18\x03 \x01(\tR\x0fresponseAddress\x12_\n\x10processing_stats\x18\x04 \x01(\x0b\x32\x34.public.llmcloud.inferencemanager.v1.ProcessingStatsR\x0fprocessingStats\x12_\n\x10generation_stats\x18\x05 \x01(\x0b\x32\x34.public.llmcloud.inferencemanager.v1.GenerationStatsR\x0fgenerationStats\x12/\n\x13generation_finished\x18\x06 \x01(\x08R\x12generationFinished\x12\x19\n\x08model_id\x18\x07 \x01(\tR\x07modelId2\xc5\x01\n\x16InferenceResultService\x12\xaa\x01\n\tGetResult\x12K.public.llmcloud.inferencemanager.v1.InferenceResultServiceGetResultRequest\x1aL.public.llmcloud.inferencemanager.v1.InferenceResultServiceGetResultResponse\"\x00(\x01\x42\xca\x02\n\'com.public.llmcloud.inferencemanager.v1B\x1bInferenceResultServiceProtoP\x01ZQgit.groq.io/cloud/go-proto/public/llmcloud/inferencemanager/v1;inferencemanagerv1\xa2\x02\x03PLI\xaa\x02#Public.Llmcloud.Inferencemanager.V1\xca\x02$Public_\\Llmcloud\\Inferencemanager\\V1\xe2\x02\x30Public_\\Llmcloud\\Inferencemanager\\V1\\GPBMetadata\xea\x02&Public::Llmcloud::Inferencemanager::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.llmcloud.inferencemanager.v1.inference_result_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.public.llmcloud.inferencemanager.v1B\033InferenceResultServiceProtoP\001ZQgit.groq.io/cloud/go-proto/public/llmcloud/inferencemanager/v1;inferencemanagerv1\242\002\003PLI\252\002#Public.Llmcloud.Inferencemanager.V1\312\002$Public_\\Llmcloud\\Inferencemanager\\V1\342\0020Public_\\Llmcloud\\Inferencemanager\\V1\\GPBMetadata\352\002&Public::Llmcloud::Inferencemanager::V1'
  _globals['_INFERENCERESULTSERVICEGETRESULTRESPONSE']._serialized_start=139
  _globals['_INFERENCERESULTSERVICEGETRESULTRESPONSE']._serialized_end=180
  _globals['_PROCESSINGSTATS']._serialized_start=182
  _globals['_PROCESSINGSTATS']._serialized_end=304
  _globals['_GENERATIONSTATS']._serialized_start=306
  _globals['_GENERATIONSTATS']._serialized_end=430
  _globals['_INFERENCERESULTSERVICEGETRESULTREQUEST']._serialized_start=433
  _globals['_INFERENCERESULTSERVICEGETRESULTREQUEST']._serialized_end=839
  _globals['_INFERENCERESULTSERVICE']._serialized_start=842
  _globals['_INFERENCERESULTSERVICE']._serialized_end=1039
# @@protoc_insertion_point(module_scope)
