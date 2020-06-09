#!/bin/sh

prefix1="../aws_cloudformation/templates"

test_validate_lambda()
{
    rm -rf tmp
    mkdir -p tmp
    cp ../aws_cloudformation/templates/validate_lambda.py ./tmp/tmpvalidate_lambda.py || \
        { echo "error in cp" && exit 1;}
    python2 main_validate_test.py
}

validate_template()
{
    local url=''
    local all_templates=''
    local template_path=''
    local file_name=

    echo "copy templates to s3"
    aws s3 cp "$prefix1/" s3://llf-bucket/ --include "*.template" --recursive  || \
        { echo "s3 copy error!"&& exit 1;}
    all_templates=`ls  $prefix1/*.template`
    for template_path in $all_templates
    do
        file_name=`basename $template_path`
        echo "validate template: $file_name"
        #aws s3 cp "$template_path" s3://llf-bucket/  >/dev/null
        url=`aws s3 presign s3://llf-bucket/$file_name`
        aws cloudformation validate-template --template-url "$url" >/dev/null
        ret=$?
        if [ 0 -ne $ret ];then
            echo "validate template($template_path) error"
            exit 1
        fi
    done

}

#test_validate_lambda
validate_template


