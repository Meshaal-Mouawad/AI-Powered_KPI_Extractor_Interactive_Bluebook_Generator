kpi flare recovery pct
==================================================

.. math::

   \text{}

.. raw:: html

   <style>
      .kpi-table {
         width: 100%; border-collapse: collapse; margin-bottom: 1.5em;
         border: 1px solid #e0e0e0; table-layout: fixed;
      }
      .kpi-table td {
         padding: 12px; vertical-align: top; border: 1px solid #e0e0e0;
         word-wrap: break-word;
      }
      .kpi-table td:first-child {
         width: 25%; font-weight: bold; background-color: #f7f7f7;
      }
      .kpi-table ul { list-style-type: disc; padding-left: 20px; margin: 0; }
      .kpi-table .math-equation {
         text-align: center; margin: 1em 0; overflow-x: auto; padding: 5px;
      }
      .kpi-table .formula-notes li { margin-bottom: 0.5em; }
      .kpi-table .formula-notes i { font-family: 'Times New Roman', serif; }
      .btn { display:inline-block; padding:8px 12px; border-radius:6px; color:#fff; text-decoration:none; font-weight:500; font-size:13px; }
      .btn-vscode { background-color:#2c5282; }
      .btn-pycharm { background-color:#000; }
      .btn-edit { background-color:#4a7c59; }
   </style>

   <div style="margin-bottom: 1.5em; display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
      <span style="font-size: 13px; font-weight: 500; color: #4a5568;">Open in:</span>
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/ana_kpi.hdbview:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project/ana_kpi.hdbview&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=kpi%20flare%20recovery%20pct" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The flare recovery percentage measures the efficiency of gas recovery from flaring operations</li><li>indicating the proportion of gas that is successfully captured and reused rather than being released into the atmosphere</li><li>Share of total gas that is recovered instead of flared</li><li>indicating the effectiveness of recovery systems</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to minimize environmental impact and maximize resource utilization by ensuring a higher percentage of gas is recovered during flaring events</li><li>Reduce flaring and emissions by improving recovery system reliability and operation</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>This KPI is calculated by dividing the volume of recovered gas by the total volume of gas flared, with the result expressed as a percentage.</p>
               <div class="math-equation">$$ \mathit{Kpi\,Flare\,Recovery\,Pct} = \frac{\mathit{Recovered\,Gas\,M3}}{\mathit{Nullif(Total\,Gas\,M3,0)}} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               8.5s (AI 8.5s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 8.486s
                  • AI: 8.486s
                  • Render: 0.0s
               </div>
            </td>
         </tr>

         <tr>
            <td>Extraction rate %</td>
            <td>100.0%</td>
         </tr>
         <tr>
            <td>Error rate %</td>
            <td>0.0%</td>
         </tr>
         <tr>
            <td>Used in KPI(s)</td>
            <td><ul><li>This KPI is used in evaluating operational efficiency and environmental performance within the oil and gas sector</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI include the volume of recovered gas and the total volume of gas flared</li><li>Gas flared volume and gas recovered volume over the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for this KPI is percentage.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for this KPI is typically sourced from operational reports and gas recovery systems within production facilities.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>A higher flare recovery percentage indicates better performance in gas management and compliance with environmental regulations.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: sql
      :linenos:
   

      SELECT (recovered_gas_m3 / NULLIF(total_gas_m3,0)) * 100 AS kpi_flare_recovery_pct