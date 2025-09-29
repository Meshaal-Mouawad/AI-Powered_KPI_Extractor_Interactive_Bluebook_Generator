Propylene to Ethylene (P/E) Ratio
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
      <a href="vscode://file//Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/dotnet_kpi.cs:0" target="_blank" class="btn btn-vscode">VS Code</a>
      <a href="pycharm://open?file=/Users/meshaalmouawad/AI-Powered_KPI_Extractor_Interactive_Bluebook_Generator/sample_project_50/dotnet_kpi.cs&line=0" target="_blank" class="btn btn-pycharm">PyCharm</a>
      <a href="/edit?kpi=Propylene%20to%20Ethylene%20%28P/E%29%20Ratio" target="_blank" class="btn btn-edit">Edit</a>
   </div>

   <table class="kpi-table">
      <tbody>
         <tr>
            <td>Description</td>
            <td><ul><li>The Propylene to Ethylene (P/E) Ratio measures the relative production of propylene compared to ethylene within a given process</li><li>The ratio of propylene to ethylene production volumes</li><li>used to assess the balance of the product slate</li></ul></td>
         </tr>
         <tr>
            <td>Objective</td>
            <td><ul><li>The objective of this KPI is to assess the efficiency of propylene production in relation to ethylene output</li><li>which is crucial for optimizing feedstock utilization and maximizing profitability</li><li>Align production strategy with market demand and margins by monitoring relative propylene versus ethylene output</li></ul></td>
         </tr>
         <tr>
            <td>Formula</td>
            <td>
               <p>The P/E Ratio is calculated by dividing the total tons of propylene produced by the total tons of ethylene produced.</p>
               <div class="math-equation">$$ \mathit{Result} = \frac{\mathit{0\,0;\,Return\,Propylene\,Produced\,Tons}}{\mathit{Ethylene\,Produced\,Tons;\,\}\,\}}} $$</div>
            </td>
         </tr>

         <tr>
            <td>Generation time</td>
            <td>
               0.0s (AI 0.0s + Render 0.0s)
               <div style="font-size: 12px; color: #6b7280; margin-top: 4px;">
                  Total: 0.003s
                  • AI: 0.001s
                  • Render: 0.002s
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
            <td><ul><li>This KPI is utilized in performance evaluations and operational assessments within petrochemical production facilities</li></ul></td>
         </tr>
         <tr>
            <td>Input Measure</td>
            <td><ul><li>The input measures for this KPI are the total tons of propylene and ethylene produced during a specified time period</li><li>Total propylene produced and total ethylene produced in the measurement period</li></ul></td>
         </tr>
         <tr>
            <td>Unit of Measure</td>
            <td>The unit of measure for the P/E Ratio is a dimensionless ratio, expressed as tons of propylene per ton of ethylene.</td>
         </tr>
         <tr>
            <td>Reporting Source</td>
            <td>Data for this KPI is sourced from production reports and operational databases within the petrochemical facility.</td>
         </tr>
         <tr>
            <td>Comments</td>
            <td>Integrating processes like olefin cracking or metathesis units can increase the overall propylene yield and thus the P/E ratio.</td>
         </tr>
      </tbody>
   </table>

.. admonition:: Code Context
   :class: dropdown

   
   
   

   .. code-block:: csharp
      :linenos:
   

      // KPI: Propylene to Ethylene (P/E) Ratio
   public static class KpiDemo
   {
       public static double ComputePERatio(double propyleneProducedTons, double ethyleneProducedTons)
       {
           if (ethyleneProducedTons == 0) return 0.0;
           return propyleneProducedTons / ethyleneProducedTons;
       }
   }