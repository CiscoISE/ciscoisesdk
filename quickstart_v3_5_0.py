#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick Start - SDK Cisco ISE v3.5.0

Script de inicio rápido para probar la conexión al SDK.
Edita las credenciales abajo y ejecuta: python quickstart_v3_5_0.py

Copyright (c) 2025 Cisco and/or its affiliates.
"""

from ciscoisesdk import IdentityServicesEngineAPI
from ciscoisesdk.exceptions import ApiError

# ============================================================
# CONFIGURA TUS CREDENCIALES AQUÍ
# ============================================================
ISE_URL = 'https://198.18.133.27'  # ← Cambia esto
ISE_USER = 'admin'                  # ← Cambia esto
ISE_PASS = 'C1sco12345'            # ← Cambia esto
# ============================================================

def main():
    print("\n" + "="*60)
    print("  Quick Start - Cisco ISE SDK v3.5.0")
    print("="*60)
    
    print(f"\n📡 Conectando a: {ISE_URL}")
    print(f"👤 Usuario: {ISE_USER}")
    
    try:
        # Crear conexión
        api = IdentityServicesEngineAPI(
            username=ISE_USER,
            password=ISE_PASS,
            base_url=ISE_URL,
            version='3.5.0',
            verify=False,
            debug=False,
            uses_api_gateway=True
        )
        
        print("✓ Conectado exitosamente!\n")
        
        # Prueba 1: Obtener versión de ISE
        print("-" * 60)
        print("📋 Prueba 1: Obtener versión de ISE")
        print("-" * 60)
        
        version_response = api.misc.get_version_info()
        version = version_response.response.VersionInfo.version
        patch = version_response.response.VersionInfo.patch
        
        print(f"✓ Versión ISE: {version}")
        print(f"✓ Patch: {patch}\n")
        
        # Prueba 2: Listar nodos
        print("-" * 60)
        print("🖥️  Prueba 2: Listar nodos ISE")
        print("-" * 60)
        
        nodes_response = api.node.get_nodes()
        nodes = nodes_response.response.response
        
        print(f"✓ Nodos encontrados: {len(nodes)}")
        for node in nodes:
            print(f"  • {node.hostname} - Roles: {', '.join(node.roles)}")
        print()
        
        # Prueba 3: Contar Network Devices
        print("-" * 60)
        print("🔧 Prueba 3: Contar Network Devices")
        print("-" * 60)
        
        devices_response = api.networkdevice.get_all(size=1)
        total = devices_response.response.SearchResult.total
        
        print(f"✓ Total de Network Devices: {total}\n")
        
        # Prueba 4: Contar Endpoints
        print("-" * 60)
        print("💻 Prueba 4: Contar Endpoints")
        print("-" * 60)
        
        endpoints_response = api.endpoint.get_all(size=1)
        total = endpoints_response.response.SearchResult.total
        
        print(f"✓ Total de Endpoints: {total}\n")
        
        # Prueba 5: Listar primeros 3 Security Group Tags
        print("-" * 60)
        print("🔐 Prueba 5: Listar Security Group Tags")
        print("-" * 60)
        
        sgts_response = api.sgt.get_all(size=3)
        sgts = sgts_response.response.SearchResult.resources
        
        print(f"✓ Primeros {len(sgts)} SGTs:")
        for sgt in sgts:
            sgt_detail = api.sgt.get_by_id(id=sgt.id).response.Sgt
            print(f"  • {sgt_detail.name} (Valor: {sgt_detail.value})")
        print()
        
        # Prueba 6: Sesiones activas
        print("-" * 60)
        print("📊 Prueba 6: Sesiones activas")
        print("-" * 60)
        
        sessions_response = api.misc.get_active_session_count()
        sessions = sessions_response.response
        
        print(f"✓ Sesiones activas: {sessions}\n")
        
        # Resumen final
        print("="*60)
        print("  ✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("="*60)
        print("\n🎉 ¡Tu SDK está funcionando correctamente!")
        print("\n📚 Próximos pasos:")
        print("   1. Revisa 'examples_v3_5_0.py' para ejemplos interactivos")
        print("   2. Ejecuta 'test_v3_5_0_sdk.py' para pruebas completas")
        print("   3. Lee 'TESTING_V3_5_0.md' para documentación detallada")
        print()
        
    except ApiError as e:
        print(f"\n❌ Error de API: {e}")
        print("\n💡 Verifica:")
        print("   • URL correcta del servidor ISE")
        print("   • Usuario y contraseña correctos")
        print("   • ERS API y OpenAPI habilitados en ISE")
        print("   • Conectividad de red\n")
        
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        print()


if __name__ == "__main__":
    main()

