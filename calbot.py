from datetime import date



today = date.today().isoformat()
print() 
with open("Calbot test results.txt", "a") as file:
        print(today, "Authorization", file=file, sep="\n")



try:
    import calbot_google_chrome 
    print()
except:        
    print()
finally:
    print('Google authorization сheckin in chrome.')
try:
    import calbot_outlook_chrome 
    print()
except:        
    print()
finally:
    print('Outlock authorization сheckin in chrome.')
try:
    import calbot_exchange_chrome 
    print()
except:        
    print()
finally:
    print('Exchange authorization сheckin in chrome.')    
try:
    import calbot_icloud_chrome 
    print()
except:        
    print()
finally:
    print('iCloud authorization сheckin in chrome.')
try:
    import calbot_google_firefox 
    print()
except:        
    print()
finally:
    print('Google authorization сheckin in firefox.')
try:
    import calbot_outlook_firefox 
    print()
except:        
    print()
finally:
    print('Outlock authorization сheckin in firefox.')
try:
    import calbot_exchange_firefox 
    print()
except:        
    print()
finally:
    print('Exchange authorization сheckin in firefox.')    
try:
    import calbot_icloud_firefox 
    print()
except:        
    print()
finally:
    print('iCloud authorization сheckin in firefox.')
try:
    import calbot_google_edge 
    print()
except:        
    print()
finally:
    print('Google authorization сheckin in edge.')
try:
    import calbot_outlook_edge 
    print()
except:        
    print()
finally:
    print('Outlock authorization сheckin in edge.')
try:
    import calbot_exchange_edge 
    print()
except:        
    print()
finally:
    print('Exchange authorization сheckin in edge.')    
try:
    import calbot_icloud_edge 
    print()
except:        
    print()
finally:
    print('iCloud authorization сheckin in edge.')
try:
    import calbot_google_brave 
    print()
except:        
    print()
finally:
    print('Google authorization сheckin in brave.')
try:
    import calbot_outlook_brave 
    print()
except:        
    print()
finally:
    print('Outlock authorization сheckin in brave.')
try:
    import calbot_exchange_brave 
    print()
except:        
    print()
finally:
    print('Exchange authorization сheckin in brave.')    
try:
    import calbot_icloud_brave 
    print()
except:        
    print()
finally:
    print('iCloud authorization сheckin in brave.')