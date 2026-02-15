import json
import time
import os
import random
import boto3
from typing import Dict, Any

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Ultra-expensive data processing function
    Designed to consume maximum memory and execution time for high costs
    """
    
    print(f"🔥 EXPENSIVE DATA PROCESSOR STARTED - Memory: {context.memory_limit_in_mb}MB")
    print(f"💸 Warning: This function is designed to maximize AWS costs!")
    
    try:
        # Simulate expensive memory-intensive operations
        expensive_data_processing()
        
        # Simulate expensive database operations
        expensive_database_operations()
        
        # Simulate expensive S3 operations
        expensive_s3_operations()
        
        # Simulate CPU-intensive work to maximize execution time
        expensive_cpu_work()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Expensive data processing completed',
                'cost_warning': 'This execution was designed to be expensive!',
                'memory_used': f"{context.memory_limit_in_mb}MB",
                'execution_time': 'Maximized for cost',
                'estimated_cost': '$50-100 per million invocations with 10GB memory'
            })
        }
        
    except Exception as e:
        print(f"Error in expensive processing: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Expensive processing failed but still incurred costs!'
            })
        }

def expensive_data_processing():
    """Simulate memory-intensive data processing"""
    print("💰 Starting expensive memory operations...")
    
    # Create large data structures to consume memory
    expensive_data = []
    for i in range(100000):  # 100k items
        expensive_data.append({
            'id': i,
            'data': 'x' * 1000,  # 1KB per item
            'timestamp': time.time(),
            'expensive_field': random.random() * 1000000,
            'nested_data': {
                'level1': {'level2': {'level3': 'expensive_nested_data' * 100}}
            }
        })
    
    # Expensive data transformations
    processed_data = []
    for item in expensive_data:
        processed_item = {
            'processed_id': item['id'] * 2,
            'processed_data': item['data'][::-1],  # Reverse string
            'expensive_calculation': sum(ord(c) for c in item['data']),
            'complex_transformation': expensive_transform(item)
        }
        processed_data.append(processed_item)
    
    print(f"📊 Processed {len(processed_data)} expensive items")

def expensive_transform(data: Dict) -> Dict:
    """Expensive data transformation"""
    result = {}
    for key, value in data.items():
        if isinstance(value, str):
            # Expensive string operations
            result[f"transformed_{key}"] = ''.join(
                chr((ord(c) + 1) % 128) for c in value
            )
        elif isinstance(value, (int, float)):
            # Expensive mathematical operations
            result[f"calc_{key}"] = sum(
                i ** 2 for i in range(int(abs(value) % 1000))
            )
        elif isinstance(value, dict):
            result[f"nested_{key}"] = expensive_transform(value)
    return result

def expensive_database_operations():
    """Simulate expensive DynamoDB operations"""
    print("💰 Starting expensive database operations...")
    
    try:
        # Simulate writing to expensive DynamoDB tables
        # (Note: In real deployment, table names would be from environment variables)
        
        # Simulate multiple expensive writes
        for i in range(100):  # 100 expensive writes
            expensive_record = {
                'record_id': f"expensive_record_{i}_{int(time.time())}",
                'large_data': 'x' * 10000,  # 10KB per record
                'timestamp': time.time(),
                'expensive_attributes': {
                    f'attr_{j}': random.random() * 1000000 
                    for j in range(50)  # 50 attributes per record
                }
            }
            
            # Simulate the write operation (would be actual DynamoDB put_item in real deployment)
            print(f"💸 Would write expensive record {i} to DynamoDB")
        
        # Simulate expensive reads with complex queries
        for i in range(50):  # 50 expensive reads
            print(f"💸 Would perform expensive DynamoDB query {i}")
            time.sleep(0.01)  # Simulate network latency
            
    except Exception as e:
        print(f"Database operations error: {e}")

def expensive_s3_operations():
    """Simulate expensive S3 operations"""
    print("💰 Starting expensive S3 operations...")
    
    try:
        # Simulate multiple S3 operations
        for i in range(20):  # 20 expensive S3 operations
            
            # Generate expensive data to upload
            expensive_content = {
                'data_id': f"expensive_data_{i}",
                'large_payload': 'x' * 100000,  # 100KB per object
                'metadata': {
                    f'meta_{j}': f"expensive_metadata_value_{j}" * 100
                    for j in range(20)
                },
                'timestamp': time.time()
            }
            
            # Simulate S3 put operation
            print(f"💸 Would upload {len(json.dumps(expensive_content))} bytes to S3")
            
            # Simulate S3 get operation  
            print(f"💸 Would download expensive object {i} from S3")
            
            time.sleep(0.01)  # Simulate network operations
            
    except Exception as e:
        print(f"S3 operations error: {e}")

def expensive_cpu_work():
    """Perform CPU-intensive work to maximize execution time and cost"""
    print("💰 Starting expensive CPU operations...")
    
    # Prime number calculation (CPU intensive)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Find expensive prime numbers
    primes = []
    for i in range(10000, 20000):  # Check 10k numbers for primality
        if is_prime(i):
            primes.append(i)
    
    print(f"🔢 Found {len(primes)} prime numbers (expensive calculation)")
    
    # Matrix multiplication (memory and CPU intensive)
    print("🔢 Performing expensive matrix operations...")
    matrix_size = 500  # 500x500 matrix
    matrix_a = [[random.random() for _ in range(matrix_size)] for _ in range(matrix_size)]
    matrix_b = [[random.random() for _ in range(matrix_size)] for _ in range(matrix_size)]
    
    # Expensive matrix multiplication
    result_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    print(f"🔢 Completed expensive {matrix_size}x{matrix_size} matrix multiplication")
    
    # Sorting large datasets (CPU and memory intensive)
    print("🔢 Performing expensive sorting operations...")
    large_dataset = [random.random() * 1000000 for _ in range(100000)]
    
    # Multiple expensive sorts
    for sort_type in ['regular', 'reverse', 'custom']:
        if sort_type == 'regular':
            sorted_data = sorted(large_dataset)
        elif sort_type == 'reverse':
            sorted_data = sorted(large_dataset, reverse=True)
        else:
            sorted_data = sorted(large_dataset, key=lambda x: (x % 7, -x))
        
        print(f"🔢 Completed expensive {sort_type} sort of {len(sorted_data)} items")

if __name__ == "__main__":
    # Test locally (will be expensive in AWS!)
    class MockContext:
        memory_limit_in_mb = 10240
        
    test_event = {"test": "expensive_local_test"}
    result = lambda_handler(test_event, MockContext())
    print(f"Test result: {result}")
