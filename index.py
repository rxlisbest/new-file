#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def str2Hump(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    for i in arr:
        res =  res + i[0].upper() + i[1:]
    return res

print str2Hump('test_test')

table_arr = {
    'form_record_exponent': "'id', 'value', 'record_id', 'form_category_id', 'created_at', 'updated_at', 'submit_user_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type'", 
    'form_record_result_ask': "'id', 'name', 'type', 'time', 'range', 'member_number', 'party_member_number', 'organization_type', 'has_committee', 'committeeman_level', 'deputy_secretary_level', 'party_member_roll', 'committeeman_condition', 'reporting_organization', 'term', 'result_mode', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_reply': "'id', 'condition', 'result', 'term', 'organization_id', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_transfer': "'id', 'party_member', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_election': "'id', 'type', 'time', 'member', 'should_member_number', 'is_valid', 'real_member_number', 'absence_explanation', 'committeeman_result', 'deputy_secretary_result', 'secretary_result', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_approval': "'id', 'result', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_file': "'id', 'vote', 'method', 'draft', 'reply', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_summary': "'id', 'time', 'organization_id', 'record_file_ids', 'plan_file_ids', 'punish_file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_meeting': "'id', 'name', 'time', 'address', 'type', 'responsible_organization_id', 'organization_id', 'presenter_id', 'attendee', 'should_member_number', 'real_member_number', 'has_result', 'file_ids', 'reference_file_ids', 'content', 'result', 'difficult', 'process', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_recommend': "'id', 'time', 'member', 'member_result', 'condition', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_learn': "'id', 'name', 'start_time', 'end_time', 'address', 'type', 'presenter_id', 'attendee', 'responsible_organization_id', 'file_ids', 'reference_file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_prepare': "'id', 'name', 'file_ids', 'condition', 'option', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_activity': "'id', 'title', 'type', 'start_time', 'end_time', 'address', 'attendee', 'organization_id', 'resource', 'file_ids', 'reference_file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_tree': "'id', 'object', 'organization_id', 'name', 'time', 'file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_condole': "'id', 'object', 'name', 'time', 'file_ids', 'type', 'object_type', 'money', 'reference_file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_money': "'id', 'object', 'name', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_punish': "'id', 'object', 'time', 'type', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_team': "'id', 'name', 'member_ids', 'organization_id', 'time', 'content', 'file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_position': "'id', 'name', 'type', 'address', 'area', 'content', 'file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_organization': "'id', 'name', 'time', 'party_member_number', 'content', 'file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_register': "'id', 'name', 'age', 'time', 'organization', 'content', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_item': "'id', 'name', 'time', 'responsible_organization_id', 'organization_id', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'", 
    'form_record_result_system': "'id', 'name', 'type', 'time', 'file_ids', 'form_category_id', 'created_at', 'updated_at', 'is_main', 'submit_user_id', 'form_id', 'process_log_id', 'process_step_log_id', 'process_step_form_relation_id', 'submit_organization_id', 'submit_role_id', 'submit_organization_type', 'exponent_id', 'record_id'"
}
print table_arr

model_template = "<?php\n\
\n\
namespace Form\Model;\n\
\n\
use Sooc\Model;\n\
\n\
/**\n\
 * Class {{class_name}}Model\n\
 * @package Form\Model\n\
 */\n\
class {{class_name}}Model extends Model\n\
{\n\
    protected $tableName = '{{table_name}}';\n\
    protected $fields = [{{field}}];\n\
\n\
    protected $_validate = array();\n\
\n\
    protected $_auto = array(\n\
        array('created_at', NOW_TIME, self::MODEL_INSERT),\n\
        array('updated_at', NOW_TIME, self::MODEL_UPDATE),\n\
    );\n\
}\n"
service_template = "<?php\n\
\n\
namespace Form\Service;\n\
\n\
use Form\Model\{{class_name}}Model;\n\
\n\
/**\n\
 * Class {{class_name}}Service\n\
 * @package Form\Service\n\
 */\n\
class {{class_name}}Service extends {{class_name}}Model\n\
{\n\
}\n"
model_dir = '/Library/WebServer/Documents/sooc_view/apps/Form/Model/'
service_dir = '/Library/WebServer/Documents/sooc_view/apps/Form/Service/'
for (i, v) in table_arr.items():
    print i
    table_name = i
    class_name = str2Hump(i)
    model_str = model_template.replace('{{table_name}}', table_name )
    model_str = model_str.replace('{{class_name}}', class_name )
    model_str = model_str.replace('{{field}}', v )
    service_str = service_template.replace('{{class_name}}', class_name )
    print model_dir + class_name + 'Model.class.php'
    print model_str
    print service_str 
    fp = open(model_dir + class_name + 'Model.class.php','w+')
    fp.write(model_str)
    fp.close()
    fp = open(service_dir + class_name + 'Service.class.php','w+')
    fp.write(service_str)
    fp.close()
