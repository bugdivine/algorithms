
int diameter(std::vector<pair<int, int> > v[], int x, int parent, int *height)
{
    int *h = (int *)malloc(sizeof(int)), h1 = 0, h2 = 0;
    int diam = 0;
    for (std::vector<pair<int, int> >::iterator it = v[x].begin(); it != v[x].end(); it++) {
        if ((*it).first == parent)
            continue;
        diam = MAX(diam, diameter(v, (*it).first, x, h));
        *h += (*it).second;
        if (*h>h2)
        {
            if (*h>h1)
            {
                h2 = h1;
                h1 = *h;
            }
            else
            {
                h2 = *h;
            }
        }
    }
    *height = MAX(h1, h2);
    return MAX(diam, h1+h2);
}
