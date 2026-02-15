import json
import time
import os
import random
import numpy as np
from typing import Dict, Any, List

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Ultra-expensive ML inference function
    Simulates heavy machine learning operations for maximum cost
    """
    
    print(f"🤖 EXPENSIVE ML INFERENCE STARTED - Memory: {context.memory_limit_in_mb}MB")
    print(f"💸 Warning: This ML function is designed to maximize AWS costs!")
    
    try:
        # Get batch size from event or use expensive default
        batch_size = event.get('batch_size', 1000)
        
        # Simulate expensive model loading
        expensive_model_loading()
        
        # Simulate expensive inference operations
        inference_results = expensive_inference_batch(batch_size)
        
        # Simulate expensive post-processing
        processed_results = expensive_post_processing(inference_results)
        
        # Simulate expensive model ensemble
        ensemble_results = expensive_model_ensemble(processed_results)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Expensive ML inference completed for batch size {batch_size}',
                'results_count': len(ensemble_results),
                'cost_warning': 'This ML inference was designed to be extremely expensive!',
                'memory_used': f"{context.memory_limit_in_mb}MB",
                'estimated_cost': '$100-200 per million invocations with 10GB memory',
                'model_info': {
                    'type': 'simulated_expensive_ensemble',
                    'models': 5,
                    'parameters': '10B+ (simulated)',
                    'inference_complexity': 'ultra-high'
                }
            })
        }
        
    except Exception as e:
        print(f"Error in expensive ML inference: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'message': 'Expensive ML inference failed but still incurred costs!'
            })
        }

def expensive_model_loading():
    """Simulate loading large, expensive ML models"""
    print("🧠 Loading expensive ML models...")
    
    # Simulate loading multiple large models
    models = []
    model_types = ['transformer', 'cnn', 'lstm', 'bert', 'gpt']
    
    for i, model_type in enumerate(model_types):
        print(f"📥 Loading expensive {model_type} model {i+1}/5...")
        
        # Simulate large model weights (consume memory)
        model_weights = {
            'layer_1': np.random.random((5000, 5000)).astype(np.float32),  # 100MB
            'layer_2': np.random.random((5000, 2000)).astype(np.float32),  # 40MB
            'layer_3': np.random.random((2000, 1000)).astype(np.float32),  # 8MB
            'embeddings': np.random.random((50000, 768)).astype(np.float32),  # 150MB
            'attention_weights': np.random.random((12, 768, 768)).astype(np.float32),  # ~27MB
        }
        
        # Simulate model configuration
        model_config = {
            'model_type': model_type,
            'parameters': sum(w.size for w in model_weights.values()),
            'memory_usage': sum(w.nbytes for w in model_weights.values()) / (1024**2),
            'loaded_at': time.time()
        }
        
        models.append({
            'weights': model_weights,
            'config': model_config
        })
        
        print(f"✅ Loaded {model_type}: {model_config['parameters']:,} parameters, "
              f"{model_config['memory_usage']:.1f}MB")
        
        # Simulate loading time
        time.sleep(0.1)
    
    print(f"🧠 All {len(models)} expensive models loaded successfully")
    return models

def expensive_inference_batch(batch_size: int) -> List[Dict]:
    """Perform expensive inference on a large batch"""
    print(f"🔮 Starting expensive inference for batch size: {batch_size}")
    
    results = []
    
    for batch_idx in range(0, batch_size, 100):  # Process in sub-batches
        current_batch_size = min(100, batch_size - batch_idx)
        
        # Generate expensive input data
        expensive_inputs = []
        for i in range(current_batch_size):
            # Simulate complex input features
            input_features = {
                'text_embedding': np.random.random(768).astype(np.float32),
                'image_features': np.random.random((224, 224, 3)).astype(np.float32),
                'numerical_features': np.random.random(1000).astype(np.float32),
                'sequence_data': np.random.random((512, 768)).astype(np.float32),
                'metadata': {
                    'input_id': f"expensive_input_{batch_idx}_{i}",
                    'complexity': 'ultra-high',
                    'processing_timestamp': time.time()
                }
            }
            expensive_inputs.append(input_features)
        
        # Simulate expensive inference computations
        batch_results = []
        for i, input_data in enumerate(expensive_inputs):
            
            # Simulate multiple expensive model predictions
            predictions = {}
            
            # Text classification (expensive)
            text_scores = expensive_text_classification(input_data['text_embedding'])
            predictions['text_classification'] = text_scores
            
            # Image recognition (expensive)
            image_scores = expensive_image_recognition(input_data['image_features'])
            predictions['image_recognition'] = image_scores
            
            # Sequence prediction (expensive)
            sequence_output = expensive_sequence_prediction(input_data['sequence_data'])
            predictions['sequence_prediction'] = sequence_output
            
            # Feature extraction (expensive)
            extracted_features = expensive_feature_extraction(input_data['numerical_features'])
            predictions['extracted_features'] = extracted_features
            
            result = {
                'input_id': input_data['metadata']['input_id'],
                'predictions': predictions,
                'confidence_scores': {
                    'overall': random.uniform(0.7, 0.99),
                    'text': random.uniform(0.6, 0.95),
                    'image': random.uniform(0.65, 0.98),
                    'sequence': random.uniform(0.7, 0.96)
                },
                'processing_time': time.time() - input_data['metadata']['processing_timestamp']
            }
            
            batch_results.append(result)
        
        results.extend(batch_results)
        print(f"✅ Processed expensive batch {batch_idx//100 + 1}, items: {len(batch_results)}")
        
        # Add small delay to simulate processing time
        time.sleep(0.01)
    
    print(f"🔮 Completed expensive inference for {len(results)} items")
    return results

def expensive_text_classification(text_embedding: np.ndarray) -> Dict:
    """Expensive text classification simulation"""
    # Simulate transformer-like operations
    attention_weights = np.random.random((12, 768, 768)).astype(np.float32)
    
    processed_embedding = text_embedding.copy()
    for layer in range(12):  # 12 transformer layers
        # Expensive attention computation
        attention = np.dot(attention_weights[layer], processed_embedding)
        processed_embedding = np.tanh(attention)  # Expensive activation
    
    # Expensive classification head
    class_scores = {}
    categories = ['positive', 'negative', 'neutral', 'urgent', 'spam', 'important']
    
    for category in categories:
        # Expensive score computation
        score = float(np.sum(processed_embedding * np.random.random(768)) / 768)
        class_scores[category] = max(0, min(1, score))
    
    return class_scores

def expensive_image_recognition(image_features: np.ndarray) -> Dict:
    """Expensive image recognition simulation"""
    h, w, c = image_features.shape
    
    # Simulate expensive CNN operations
    conv_layers = []
    current_features = image_features
    
    for i in range(5):  # 5 convolutional layers
        # Expensive convolution simulation
        kernel_size = 3
        filters = 64 * (2 ** i)  # Increasing filter count
        
        # Simulate convolution (expensive)
        new_h, new_w = max(1, h // 2), max(1, w // 2)
        conv_output = np.random.random((new_h, new_w, filters)).astype(np.float32)
        
        # Expensive pooling
        pooled_output = np.mean(conv_output, axis=(0, 1))  # Global average pooling simulation
        conv_layers.append(pooled_output)
        
        current_features = conv_output
        h, w = new_h, new_w
    
    # Expensive classification
    final_features = np.concatenate(conv_layers)
    
    # Simulate object detection
    objects = {}
    object_classes = ['person', 'car', 'building', 'tree', 'sign', 'animal']
    
    for obj_class in object_classes:
        # Expensive detection score
        detection_score = float(np.mean(final_features * np.random.random(len(final_features))))
        objects[obj_class] = {
            'confidence': max(0, min(1, detection_score)),
            'bbox': [random.uniform(0, 1) for _ in range(4)]  # Random bounding box
        }
    
    return objects

def expensive_sequence_prediction(sequence_data: np.ndarray) -> Dict:
    """Expensive sequence prediction simulation"""
    seq_len, feature_dim = sequence_data.shape
    
    # Simulate LSTM/GRU processing
    hidden_states = []
    hidden_size = 512
    
    current_hidden = np.zeros(hidden_size).astype(np.float32)
    
    for t in range(seq_len):
        # Expensive LSTM computation simulation
        input_features = sequence_data[t]
        
        # Simulate gates (expensive)
        forget_gate = 1 / (1 + np.exp(-(np.dot(input_features[:hidden_size], 
                                              np.random.random(hidden_size)) + 
                                      np.dot(current_hidden, np.random.random(hidden_size)))))
        
        input_gate = 1 / (1 + np.exp(-(np.dot(input_features[:hidden_size], 
                                             np.random.random(hidden_size)) + 
                                     np.dot(current_hidden, np.random.random(hidden_size)))))
        
        # Update hidden state (expensive)
        candidate = np.tanh(np.dot(input_features[:hidden_size], np.random.random(hidden_size)) + 
                           np.dot(current_hidden, np.random.random(hidden_size)))
        
        current_hidden = forget_gate * current_hidden + input_gate * candidate
        hidden_states.append(current_hidden.copy())
    
    # Generate predictions from final hidden state
    predictions = {
        'next_sequence': current_hidden[:100].tolist(),  # Predict next 100 features
        'sequence_class': {
            'anomaly': float(np.mean(current_hidden[:128])),
            'trend': 'increasing' if np.mean(current_hidden[128:256]) > 0 else 'decreasing',
            'volatility': float(np.std(current_hidden[256:384]))
        },
        'attention_weights': [float(np.mean(h)) for h in hidden_states[-10:]]  # Last 10 steps
    }
    
    return predictions

def expensive_feature_extraction(numerical_features: np.ndarray) -> Dict:
    """Expensive feature extraction and engineering"""
    
    # Expensive feature transformations
    transformed_features = {}
    
    # Polynomial features (expensive)
    poly_features = []
    for degree in range(2, 5):  # Degrees 2-4
        for i in range(0, len(numerical_features), 10):  # Sample features
            for j in range(i+1, min(i+10, len(numerical_features))):
                poly_feature = numerical_features[i] ** degree + numerical_features[j] ** degree
                poly_features.append(float(poly_feature))
    
    transformed_features['polynomial'] = poly_features[:100]  # Limit size
    
    # Statistical features (expensive)
    window_sizes = [5, 10, 20, 50]
    statistical_features = {}
    
    for window_size in window_sizes:
        windowed_stats = []
        for i in range(0, len(numerical_features) - window_size + 1, window_size):
            window = numerical_features[i:i+window_size]
            stats = {
                'mean': float(np.mean(window)),
                'std': float(np.std(window)),
                'skew': float(np.mean(((window - np.mean(window)) / np.std(window)) ** 3)),
                'kurtosis': float(np.mean(((window - np.mean(window)) / np.std(window)) ** 4))
            }
            windowed_stats.append(stats)
        statistical_features[f'window_{window_size}'] = windowed_stats
    
    transformed_features['statistical'] = statistical_features
    
    # Frequency domain features (expensive)
    fft_features = np.fft.fft(numerical_features)
    freq_features = {
        'dominant_frequency': float(np.argmax(np.abs(fft_features))),
        'spectral_energy': float(np.sum(np.abs(fft_features) ** 2)),
        'spectral_centroid': float(np.sum(np.arange(len(fft_features)) * np.abs(fft_features)) / 
                                 np.sum(np.abs(fft_features)))
    }
    
    transformed_features['frequency'] = freq_features
    
    return transformed_features

def expensive_post_processing(inference_results: List[Dict]) -> List[Dict]:
    """Expensive post-processing of inference results"""
    print("🔧 Starting expensive post-processing...")
    
    processed_results = []
    
    for result in inference_results:
        # Expensive result refinement
        processed_result = result.copy()
        
        # Expensive confidence calibration
        calibrated_scores = {}
        for pred_type, scores in result['predictions'].items():
            if isinstance(scores, dict):
                calibrated = {}
                for key, score in scores.items():
                    if isinstance(score, (int, float)):
                        # Expensive calibration function
                        calibrated_score = 1 / (1 + np.exp(-5 * (score - 0.5)))  # Sigmoid calibration
                        calibrated[key] = float(calibrated_score)
                    else:
                        calibrated[key] = score
                calibrated_scores[pred_type] = calibrated
            else:
                calibrated_scores[pred_type] = scores
        
        processed_result['calibrated_predictions'] = calibrated_scores
        
        # Expensive uncertainty quantification
        uncertainty_scores = {}
        for pred_type in result['predictions']:
            # Simulate expensive uncertainty computation
            epistemic_uncertainty = random.uniform(0.01, 0.2)
            aleatoric_uncertainty = random.uniform(0.01, 0.15)
            total_uncertainty = epistemic_uncertainty + aleatoric_uncertainty
            
            uncertainty_scores[pred_type] = {
                'epistemic': epistemic_uncertainty,
                'aleatoric': aleatoric_uncertainty,
                'total': total_uncertainty
            }
        
        processed_result['uncertainties'] = uncertainty_scores
        
        # Expensive explainability features
        explanations = {}
        for pred_type in result['predictions']:
            # Simulate expensive SHAP-like explanations
            feature_importance = {
                f'feature_{i}': random.uniform(-0.5, 0.5) 
                for i in range(20)
            }
            explanations[pred_type] = {
                'feature_importance': feature_importance,
                'explanation_method': 'simulated_expensive_shap',
                'computation_cost': 'high'
            }
        
        processed_result['explanations'] = explanations
        
        processed_results.append(processed_result)
    
    print(f"🔧 Completed expensive post-processing for {len(processed_results)} results")
    return processed_results

def expensive_model_ensemble(processed_results: List[Dict]) -> List[Dict]:
    """Expensive ensemble of multiple model predictions"""
    print("🎭 Starting expensive model ensemble...")
    
    ensemble_results = []
    
    for result in processed_results:
        # Expensive ensemble computation
        ensemble_result = result.copy()
        
        # Simulate predictions from 5 different expensive models
        model_predictions = {}
        model_names = ['transformer_v1', 'transformer_v2', 'cnn_ensemble', 'lstm_deep', 'bert_large']
        
        for model_name in model_names:
            # Generate expensive model-specific predictions
            model_pred = {}
            for pred_type, original_pred in result['predictions'].items():
                if isinstance(original_pred, dict):
                    # Add expensive noise and variation
                    model_specific = {}
                    for key, value in original_pred.items():
                        if isinstance(value, (int, float)):
                            noise = random.uniform(-0.1, 0.1)
                            model_specific[key] = max(0, min(1, value + noise))
                        else:
                            model_specific[key] = value
                    model_pred[pred_type] = model_specific
                else:
                    model_pred[pred_type] = original_pred
            
            model_predictions[model_name] = model_pred
        
        # Expensive ensemble aggregation
        ensemble_pred = {}
        for pred_type in result['predictions']:
            if isinstance(result['predictions'][pred_type], dict):
                ensemble_pred[pred_type] = {}
                for key in result['predictions'][pred_type]:
                    if isinstance(result['predictions'][pred_type][key], (int, float)):
                        # Weighted ensemble (expensive computation)
                        weights = [0.25, 0.20, 0.20, 0.20, 0.15]  # Different model weights
                        ensemble_score = sum(
                            weights[i] * model_predictions[model_names[i]][pred_type].get(key, 0)
                            for i in range(len(model_names))
                        )
                        ensemble_pred[pred_type][key] = float(ensemble_score)
                    else:
                        ensemble_pred[pred_type][key] = result['predictions'][pred_type][key]
            else:
                ensemble_pred[pred_type] = result['predictions'][pred_type]
        
        ensemble_result['ensemble_predictions'] = ensemble_pred
        ensemble_result['individual_model_predictions'] = model_predictions
        ensemble_result['ensemble_metadata'] = {
            'models_used': len(model_names),
            'ensemble_method': 'weighted_average',
            'computation_complexity': 'ultra_high'
        }
        
        ensemble_results.append(ensemble_result)
    
    print(f"🎭 Completed expensive ensemble for {len(ensemble_results)} results")
    return ensemble_results

if __name__ == "__main__":
    # Test locally (will be expensive in AWS!)
    class MockContext:
        memory_limit_in_mb = 10240
        
    test_event = {"batch_size": 10, "test": "expensive_ml_test"}
    result = lambda_handler(test_event, MockContext())
    print(f"Test result keys: {list(json.loads(result['body']).keys())}")
