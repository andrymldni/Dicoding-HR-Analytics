# Menggunakan image resmi Metabase
FROM metabase/metabase:latest

# Set environment variable Railway (Railway secara otomatis mengatur env vars penting seperti POSTGRES_HOST)
ENV MB_DB_TYPE=postgres
ENV MB_DB_DBNAME=postgres
ENV MB_DB_PORT=6543
ENV MB_DB_USER=postgres.xmkorqdrdzuuqziprgxf
ENV MB_DB_PASS=XSma7DXcyHTUIJ50
ENV MB_DB_HOST=aws-0-ap-southeast-1.pooler.supabase.com

# Port yang digunakan oleh Metabase (Railway akan menangani port forwarding)
EXPOSE 3000
