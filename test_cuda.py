import torch

def check_cuda():
    results = {}
    
    try:
        results['cuda_available'] = torch.cuda.is_available()
    except Exception as e:
        results['cuda_available'] = f"Error: {e}"
    
    try:
        results['device_count'] = torch.cuda.device_count()
    except Exception as e:
        results['device_count'] = f"Error: {e}"
    
    try:
        results['current_device'] = torch.cuda.current_device()
    except Exception as e:
        results['current_device'] = f"Error: {e}"
    
    try:
        results['device'] = torch.cuda.device(0)
    except Exception as e:
        results['device'] = f"Error: {e}"
    
    try:
        results['device_name'] = torch.cuda.get_device_name(0)
    except Exception as e:
        results['device_name'] = f"Error: {e}"
    
    return results

if __name__ == "__main__":
    cuda_results = check_cuda()
    for key, value in cuda_results.items():
        print(f"{key}: {value}")