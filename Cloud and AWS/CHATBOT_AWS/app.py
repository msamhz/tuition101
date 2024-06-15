import boto3
import botocore.config 
import json
from datetime import datetime

def generate_summary(query: str) -> str:
    prompt=f"""<s>[INST]Human: Provide a concise and accurate response as a search engine would {query}
    Assistant:[/INST]
    """
    
    body = {
        'prompt': prompt,
        'max_gen_len': 512,
        'temperature': 0.6,
        "top_p": 0.9
    }
    
    try: 
        bedrock=boto3.client("bedrock-runtime",region_name="us-east-1",
                             config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        response=bedrock.invoke_model(body=json.dumps(body),modelId="meta.llama3-70b-instruct-v1:0")
        
        response_content=response.get('body').read()
        response_data=json.loads(response_content)
        print(response_data)
        blog_details=response_data['generation']
        return blog_details
    
    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""
    
def save_blog_details_s3(s3_key,s3_bucket,generate_summary):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body = generate_summary)
        print("Code saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")
        
def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    query=event['query']

    summarised_query=generate_summary(query=query)

    if summarised_query:
        current_time=datetime.now().strftime('%H%M%S')
        s3_key=f"query-summarised/{current_time}.txt"  # current output 
        s3_bucket='awsbuckettest1211' # bucket name 
        save_blog_details_s3(s3_key,s3_bucket,summarised_query)


    else:
        print("No query was found")

    return{
        'statusCode':200,
        'body':json.dumps('Summariser in key points is completed')
    }